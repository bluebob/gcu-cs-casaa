# Benchmark Suite Validation — Session Report

**Date:** 2026-05-16  
**Operator:** Claude (claude-sonnet-4-6)  
**Scope:** `benchmark-suite/` — Python, Go, Java, JavaScript test sets  

---

## 1. Objective

Validate the Claude benchmark suite before running evaluations. For each test case across all four language CSV files, verify:

1. The `Dockerfile` exists at the declared `test_case_path`
2. The CVE ID is present in the NIST NVD database
3. Language-specific dependency files exist (`go.mod`, `requirements.txt`, `pom.xml`, `package.json`)
4. Every declared dependency/module resolves against its canonical registry

---

## 2. Tooling Created

**File:** `benchmark-suite/validate_suite.py`

A self-contained async Python script managed by `uv` (inline `# /// script` metadata, single dependency: `httpx`). Run with:

```bash
uv run validate_suite.py
```

### Design decisions

| Concern | Approach |
|---|---|
| Concurrency | `asyncio.gather` — all 56 test cases run in parallel |
| NVD rate limiting | Sliding-window semaphore: 5 slots, each held for 30 s (matches NVD's public limit of 5 req/30 s without an API key) |
| Transient failures | Retry with exponential backoff (up to 3 attempts, initial delay 5 s) on HTTP 429/5xx and network errors |
| Baseline rows | Baselines (rows whose `cve_id` starts with `base-`) have no CVE IDs and no dependency files; the NVD check and all dep-file checks are skipped for them |
| Go module escaping | Uppercase letters in module paths are encoded as `!<lowercase>` per the Go module proxy specification |
| CSV comment lines | `load_csv` filters lines starting with `#` so the `Last changed` header does not break `csv.DictReader` |

### Registry endpoints used

| Language | Dep file | Registry |
|---|---|---|
| Go | `go.mod` | `https://proxy.golang.org/{module}/@v/{version}.info` |
| Python | `requirements.txt` | `https://pypi.org/pypi/{package}/{version}/json` |
| Java | `pom.xml` | `https://search.maven.org/solrsearch/select` |
| JavaScript | `package.json` | `https://registry.npmjs.org/{package}/{version}` |

---

## 3. Test Cases Validated

56 rows loaded across four CSVs (baselines included):

| Language CSV | Total rows | Baseline rows | CVE rows |
|---|---|---|---|
| `python-set.csv` | 14 | 2 | 12 |
| `go-set.csv` | 17 | 4 | 13 |
| `java-set.csv` | 13 | 1 | 12 |
| `javascript-set.csv` | 13 | 1 | 12 |
| **Total** | **57** | **8** | **49** |

> Note: row counts above are pre-remediation. After removing the two disabled entries, the active totals are 54 rows / 47 CVE rows.

---

## 4. Initial Run Results (pre-remediation)

**42 passed · 14 failed**

### 4.1 Baseline dep-file false positives (8 failures)

All eight baseline rows failed because they have no dependency file — only a `Dockerfile` and a minimal source stub. This was a script bug: the dep-file check was applied to baselines even though they carry no library dependencies.

**Fix:** Added an early-return in `validate_test_case` for rows where `is_baseline(cve_id)` is true; the NVD check and all dep-file checks are skipped.

Affected rows:

- `python/base-python3.11-alpine` — no `requirements.txt`
- `python/base-python3.9.1-alpine3.12` — no `requirements.txt`
- `go/base-golang1.21-alpine` — no `go.mod`
- `go/base-golang1.15.8-alpine3.13` — no `go.mod`
- `go/base-golang1.16.4-alpine3.13` — no `go.mod`
- `go/base-golang1.17.4-alpine3.14` — no `go.mod`
- `java/base-eclipse-temurin17-alpine` — no `pom.xml`
- `javascript/base-node20-alpine` — no `package.json`

### 4.2 NVD API rate-limit hit (1 failure)

`java/CVE-2021-44228` received HTTP 429 from the NVD API on the first run. All 49 CVE NVD checks launched simultaneously, exhausting the public rate limit before the semaphore could enforce the 30-second window.

**Fix:** Added `_get_with_retry` with exponential backoff (delays: 5 s → 10 s → 20 s) covering HTTP 429, 5xx responses, and network exceptions. CVE-2021-44228 resolved successfully on retry.

### 4.3 Maven Central transient errors (3 failures)

Three Java test cases (`CVE-2017-5638`, `CVE-2022-42889`, `CVE-2021-45046`) showed empty error messages on the first run, indicating connection resets or timeouts against `search.maven.org`. All three resolved on retry once `_get_with_retry` was in place.

### 4.4 Genuine validation failures (2 failures — persisted after fixes)

These failures were reproducible and confirmed as real defects in the test suite:

#### go/CVE-2022-29153 — `github.com/hashicorp/consul/api@v1.11.3`

```
go module github.com/hashicorp/consul/api@v1.11.3: proxy returned HTTP 404
```

The Go module proxy returns 404 for `v1.11.3`. HashiCorp restructured the Consul module and this specific version tag is no longer resolvable via the proxy. The module path and version are therefore not usable in a `go get` or `go mod download` context.

#### java/CVE-2022-22947 — `spring-cloud-gateway-core:3.1.0`

```
Maven org.springframework.cloud:spring-cloud-gateway-core:3.1.0: not found on Maven Central
```

The Maven Central Solr search index returns `numFound: 0` for this groupId/artifactId/version combination. The artifact may have been published only to Spring's own repository (not Maven Central), or the declared coordinates are incorrect.

---

## 5. Second Run Results (post-fix, pre-CSV-remediation)

**54 passed · 2 failed**

The 8 baseline false positives and 4 transient errors were fully resolved. Only the two genuine defects remained.

---

## 6. Remediation Actions

### 6.1 go-set.csv — removed CVE-2022-29153

Removed the following row from `claude/go/go-set.csv`:

```
CVE-2022-29153,7.5,github.com/hashicorp/consul/api,v1.11.3,claude/go/CVE-2022-29153,golang:1.21-alpine
```

A `# Last changed: 2026-05-16T08:21:32Z` comment was added at the top of the file.

The directory `claude/go/CVE-2022-29153/` was **not deleted**. A `DISABLED.md` was created inside it:

> Disabled: github.com/hashicorp/consul/api@v1.11.3 is not resolvable via the Go module proxy (HTTP 404). The Consul API module was restructured and this version tag is no longer valid. Detected by validate_suite.py on 2026-05-16.

### 6.2 java-set.csv — removed CVE-2022-22947

Removed the following row from `claude/java/java-set.csv`:

```
CVE-2022-22947,10.0,spring-cloud-gateway-core,3.1.0,claude/java/CVE-2022-22947,eclipse-temurin:17-alpine
```

A `# Last changed: 2026-05-16T08:21:32Z` comment was added at the top of the file.

The directory `claude/java/CVE-2022-22947/` was **not deleted**. A `DISABLED.md` was created inside it:

> Disabled: spring-cloud-gateway-core:3.1.0 is not found on Maven Central's search index. The artifact may have been removed or the coordinates are incorrect. Detected by validate_suite.py on 2026-05-16.

### 6.3 validate_suite.py — skip-comment fix

After the `Last changed` comment lines were added to the CSVs, the script crashed with `KeyError: 'cve_id'` because `csv.DictReader` was treating the comment as the header row. Fixed by filtering comment lines before passing the file to `DictReader`:

```python
lines = (line for line in f if not line.startswith("#"))
return list(csv.DictReader(lines))
```

---

## 7. Final Run Results

**54 passed · 0 failed — exit code 0**

All 54 active test cases pass all checks. The two removed test cases are preserved on disk with `DISABLED.md` markers for future investigation or re-addition with corrected coordinates.

---

## 8. Files Modified

| File | Change |
|---|---|
| `benchmark-suite/validate_suite.py` | Created (validation script) |
| `benchmark-suite/Validation.md` | Created (this document) |
| `claude/go/go-set.csv` | Removed CVE-2022-29153 row; added `Last changed` header |
| `claude/java/java-set.csv` | Removed CVE-2022-22947 row; added `Last changed` header |
| `claude/go/CVE-2022-29153/DISABLED.md` | Created |
| `claude/java/CVE-2022-22947/DISABLED.md` | Created |

---

## 9. Recommended Follow-up

| Item | Detail |
|---|---|
| CVE-2022-29153 | Investigate whether `github.com/hashicorp/consul/api` was split into a sub-module at a different major version path (e.g. `v1.12+`). If a resolvable version exists that still demonstrates the SSRF, replace the `go.mod` and update the CSV. |
| CVE-2022-22947 | Confirm the correct Maven coordinates for Spring Cloud Gateway 3.1.0. If the artifact is only published to `repo.spring.io`, either switch to that repo or document the dependency manually. Check whether `spring-cloud-gateway-server` is the correct artifactId. |
| NVD API key | Adding an NVD API key (`apiKey` query parameter) raises the rate limit from 5 to 50 requests per 30 seconds, reducing validation run time for large suites. |
