#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
# ]
# ///

import asyncio
import csv
import json
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

import httpx

SCRIPT_DIR = Path(__file__).parent

_RETRY_STATUSES = {429, 500, 502, 503, 504}
_MAX_RETRIES = 3


async def _get_with_retry(
    client: httpx.AsyncClient, url: str, timeout: float = 30
) -> httpx.Response:
    delay = 5.0
    for attempt in range(_MAX_RETRIES):
        try:
            r = await client.get(url, timeout=timeout)
            if r.status_code not in _RETRY_STATUSES or attempt == _MAX_RETRIES - 1:
                return r
        except (httpx.TimeoutException, httpx.ConnectError, httpx.ReadError):
            if attempt == _MAX_RETRIES - 1:
                raise
        await asyncio.sleep(delay)
        delay *= 2
    return r  # unreachable, satisfies type checker


@dataclass
class CheckResult:
    name: str
    passed: bool
    message: str = ""


@dataclass
class TestCaseResult:
    cve_id: str
    language: str
    test_case_path: str
    checks: list[CheckResult] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return all(c.passed for c in self.checks)


class NVDRateLimiter:
    """Sliding window: 5 requests per 30 s (NVD public limit without API key)."""

    def __init__(self):
        self._sem = asyncio.Semaphore(5)

    async def __aenter__(self):
        await self._sem.acquire()
        return self

    async def __aexit__(self, *_):
        async def _release():
            await asyncio.sleep(30)
            self._sem.release()

        asyncio.create_task(_release())


_nvd_limiter: NVDRateLimiter | None = None


def is_baseline(cve_id: str) -> bool:
    return cve_id.startswith("base-")


# ---------------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------------


def check_dockerfile(test_path: Path) -> CheckResult:
    dockerfile = test_path / "Dockerfile"
    if dockerfile.exists():
        return CheckResult("Dockerfile exists", True)
    return CheckResult("Dockerfile exists", False, f"not found at {dockerfile}")


async def check_nvd_cve(client: httpx.AsyncClient, cve_id: str) -> CheckResult:
    async with _nvd_limiter:
        url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}"
        try:
            r = await _get_with_retry(client, url)
            if r.status_code == 200:
                if r.json().get("totalResults", 0) > 0:
                    return CheckResult(f"CVE {cve_id} in NVD", True)
                return CheckResult(f"CVE {cve_id} in NVD", False, "not found in NVD")
            return CheckResult(f"CVE {cve_id} in NVD", False, f"HTTP {r.status_code}")
        except Exception as e:
            return CheckResult(f"CVE {cve_id} in NVD", False, f"{type(e).__name__}: {e}")


# ---------------------------------------------------------------------------
# Go
# ---------------------------------------------------------------------------


def _go_escape(module: str) -> str:
    return re.sub(r"[A-Z]", lambda m: f"!{m.group(0).lower()}", module)


def _parse_go_mod(go_mod: Path) -> list[tuple[str, str]]:
    content = go_mod.read_text()
    deps: list[tuple[str, str]] = []

    # Single-line: require module version
    for m in re.finditer(r"^require\s+(\S+)\s+(\S+)", content, re.MULTILINE):
        deps.append((m.group(1), m.group(2)))

    # Block: require ( ... )
    block = re.search(r"require\s*\(([^)]+)\)", content, re.DOTALL)
    if block:
        for line in block.group(1).splitlines():
            line = line.strip()
            if line and not line.startswith("//"):
                parts = line.split()
                if len(parts) >= 2:
                    deps.append((parts[0], parts[1]))

    return deps


async def _check_go_module(
    client: httpx.AsyncClient, module: str, version: str
) -> CheckResult:
    url = f"https://proxy.golang.org/{_go_escape(module)}/@v/{version}.info"
    try:
        r = await _get_with_retry(client, url)
        if r.status_code == 200:
            return CheckResult(f"go module {module}@{version}", True)
        return CheckResult(
            f"go module {module}@{version}",
            False,
            f"proxy returned HTTP {r.status_code}",
        )
    except Exception as e:
        return CheckResult(f"go module {module}@{version}", False, f"{type(e).__name__}: {e}")


async def check_go_deps(
    client: httpx.AsyncClient, test_path: Path
) -> list[CheckResult]:
    go_mod = test_path / "go.mod"
    if not go_mod.exists():
        return [CheckResult("go.mod exists", False, f"not found at {go_mod}")]

    results = [CheckResult("go.mod exists", True)]
    deps = _parse_go_mod(go_mod)
    if deps:
        results.extend(
            await asyncio.gather(*[_check_go_module(client, m, v) for m, v in deps])
        )
    return results


# ---------------------------------------------------------------------------
# Python
# ---------------------------------------------------------------------------


def _parse_requirements(req: Path) -> list[tuple[str, str]]:
    deps = []
    for line in req.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "==" in line:
            pkg, ver = line.split("==", 1)
            deps.append((pkg.strip(), ver.strip()))
    return deps


async def _check_pypi(
    client: httpx.AsyncClient, package: str, version: str
) -> CheckResult:
    url = f"https://pypi.org/pypi/{package}/{version}/json"
    try:
        r = await _get_with_retry(client, url)
        if r.status_code == 200:
            return CheckResult(f"PyPI {package}=={version}", True)
        return CheckResult(
            f"PyPI {package}=={version}", False, f"HTTP {r.status_code}"
        )
    except Exception as e:
        return CheckResult(f"PyPI {package}=={version}", False, f"{type(e).__name__}: {e}")


async def check_python_deps(
    client: httpx.AsyncClient, test_path: Path
) -> list[CheckResult]:
    req = test_path / "requirements.txt"
    if not req.exists():
        return [CheckResult("requirements.txt exists", False, f"not found at {req}")]

    results = [CheckResult("requirements.txt exists", True)]
    deps = _parse_requirements(req)
    if deps:
        results.extend(
            await asyncio.gather(*[_check_pypi(client, p, v) for p, v in deps])
        )
    return results


# ---------------------------------------------------------------------------
# Java
# ---------------------------------------------------------------------------


def _parse_pom(pom: Path) -> list[tuple[str, str, str]]:
    tree = ET.parse(pom)
    root = tree.getroot()
    ns_match = re.match(r"\{([^}]+)\}", root.tag)
    ns = f"{{{ns_match.group(1)}}}" if ns_match else ""

    deps = []
    for dep in root.iter(f"{ns}dependency"):
        g = (dep.findtext(f"{ns}groupId") or "").strip()
        a = (dep.findtext(f"{ns}artifactId") or "").strip()
        v = (dep.findtext(f"{ns}version") or "").strip()
        if g and a and v:
            deps.append((g, a, v))
    return deps


async def _check_maven(
    client: httpx.AsyncClient, group_id: str, artifact_id: str, version: str
) -> CheckResult:
    url = (
        f"https://search.maven.org/solrsearch/select"
        f"?q=g:{group_id}+AND+a:{artifact_id}+AND+v:{version}&rows=1&wt=json"
    )
    try:
        r = await _get_with_retry(client, url)
        if r.status_code == 200:
            if r.json().get("response", {}).get("numFound", 0) > 0:
                return CheckResult(
                    f"Maven {group_id}:{artifact_id}:{version}", True
                )
            return CheckResult(
                f"Maven {group_id}:{artifact_id}:{version}",
                False,
                "not found on Maven Central",
            )
        return CheckResult(
            f"Maven {group_id}:{artifact_id}:{version}", False, f"HTTP {r.status_code}"
        )
    except Exception as e:
        return CheckResult(
            f"Maven {group_id}:{artifact_id}:{version}", False, f"{type(e).__name__}: {e}"
        )


async def check_java_deps(
    client: httpx.AsyncClient, test_path: Path
) -> list[CheckResult]:
    pom = test_path / "pom.xml"
    if not pom.exists():
        return [CheckResult("pom.xml exists", False, f"not found at {pom}")]

    results = [CheckResult("pom.xml exists", True)]
    deps = _parse_pom(pom)
    if deps:
        results.extend(
            await asyncio.gather(*[_check_maven(client, g, a, v) for g, a, v in deps])
        )
    return results


# ---------------------------------------------------------------------------
# JavaScript
# ---------------------------------------------------------------------------


def _parse_package_json(pkg: Path) -> list[tuple[str, str]]:
    data = json.loads(pkg.read_text())
    return list(data.get("dependencies", {}).items())


async def _check_npm(
    client: httpx.AsyncClient, package: str, version: str
) -> CheckResult:
    url = f"https://registry.npmjs.org/{package}/{version}"
    try:
        r = await _get_with_retry(client, url)
        if r.status_code == 200:
            return CheckResult(f"npm {package}@{version}", True)
        return CheckResult(f"npm {package}@{version}", False, f"HTTP {r.status_code}")
    except Exception as e:
        return CheckResult(f"npm {package}@{version}", False, f"{type(e).__name__}: {e}")


async def check_js_deps(
    client: httpx.AsyncClient, test_path: Path
) -> list[CheckResult]:
    pkg = test_path / "package.json"
    if not pkg.exists():
        return [CheckResult("package.json exists", False, f"not found at {pkg}")]

    results = [CheckResult("package.json exists", True)]
    deps = _parse_package_json(pkg)
    if deps:
        results.extend(
            await asyncio.gather(*[_check_npm(client, n, v) for n, v in deps])
        )
    return results


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

DEP_CHECKERS = {
    "go": check_go_deps,
    "python": check_python_deps,
    "java": check_java_deps,
    "javascript": check_js_deps,
}


async def validate_test_case(
    client: httpx.AsyncClient,
    language: str,
    cve_id: str,
    test_case_path: str,
) -> TestCaseResult:
    result = TestCaseResult(
        cve_id=cve_id, language=language, test_case_path=test_case_path
    )
    test_path = SCRIPT_DIR / test_case_path

    result.checks.append(check_dockerfile(test_path))

    # Baselines have no CVE ID and no dependency files — skip those checks.
    if is_baseline(cve_id):
        return result

    coros: list = [check_nvd_cve(client, cve_id), DEP_CHECKERS[language](client, test_path)]
    gathered = await asyncio.gather(*coros)
    for item in gathered:
        if isinstance(item, CheckResult):
            result.checks.append(item)
        else:
            result.checks.extend(item)

    return result


def load_csv(language: str) -> list[dict]:
    path = SCRIPT_DIR / "claude" / language / f"{language}-set.csv"
    with open(path, newline="") as f:
        lines = (line for line in f if not line.startswith("#"))
        return list(csv.DictReader(lines))


def print_report(results: list[TestCaseResult]) -> None:
    passed = sum(1 for r in results if r.passed)
    failed = sum(1 for r in results if not r.passed)

    print(f"\n{'=' * 70}")
    print(f"VALIDATION REPORT  |  {passed} passed  |  {failed} failed")
    print(f"{'=' * 70}")

    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"\n[{status}] {result.language}/{result.cve_id}")
        if not result.passed:
            for check in result.checks:
                if not check.passed:
                    print(f"       ✗ {check.name}: {check.message}")

    print(f"\n{'=' * 70}")
    print(f"Total: {len(results)}  |  Passed: {passed}  |  Failed: {failed}")
    print(f"{'=' * 70}\n")


async def main() -> int:
    global _nvd_limiter
    _nvd_limiter = NVDRateLimiter()

    languages = ["python", "go", "java", "javascript"]
    tasks = []

    async with httpx.AsyncClient(follow_redirects=True) as client:
        for lang in languages:
            for row in load_csv(lang):
                cve_id = row["cve_id"].strip()
                test_case_path = row["test_case_path"].strip()
                tasks.append(validate_test_case(client, lang, cve_id, test_case_path))

        print(f"Validating {len(tasks)} test cases …")
        results = await asyncio.gather(*tasks)

    print_report(list(results))
    return 1 if any(not r.passed for r in results) else 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
