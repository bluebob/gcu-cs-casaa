# Python Vulnerability Test Set

## Vulnerabilities

### CVE-2020-14343 — PyYAML Arbitrary Code Execution
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** PyYAML
- **Affected Version:** 5.3.1
- **Description:** PyYAML's `full_load` / `FullLoader` allows arbitrary code execution via the `python/object/new` constructor when processing untrusted YAML. Fixed in 5.4.

### CVE-2021-34552 — Pillow Buffer Overflow
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** Pillow
- **Affected Version:** 8.2.0
- **Description:** A buffer overflow in Pillow's `convert` function can be triggered via controlled parameters, enabling remote code execution. Fixed in 8.3.0.

### CVE-2022-37454 — SHA-3 Integer Overflow (XKCP)
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** pysha3
- **Affected Version:** 1.0.2
- **Description:** Integer overflow in the XKCP SHA-3 reference implementation's sponge function allows attackers to execute arbitrary code or eliminate expected cryptographic properties. Affects all pysha3 versions.

### CVE-2019-13132 — pyzmq Heap Buffer Overflow
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** pyzmq
- **Affected Version:** 18.0.2
- **Description:** A buffer overflow in libzmq (bundled by pyzmq) when CURVE encryption is enabled allows an unauthenticated remote client to overwrite stack memory, potentially leading to code execution.

### CVE-2021-3177 — Python ctypes Buffer Overflow
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** Python runtime (CPython)
- **Affected Version:** 3.9.1
- **Description:** Unsafe use of `sprintf` in `PyCArg_repr` within the `ctypes` module allows a buffer overflow when processing attacker-controlled floating-point values. Fixed in 3.9.2.
- **Note:** Requires non-standard base image `python:3.9.1-alpine3.12`; see summary table.

### CVE-2022-24303 — Pillow Temporary File Deletion
- **CVSS Score:** 9.1 (CRITICAL, v3.1)
- **Affected Library:** Pillow
- **Affected Version:** 9.0.0
- **Description:** Improper handling of whitespace in temporary file paths allows attackers to delete arbitrary files on the system. Fixed in 9.0.1.

### CVE-2023-43804 — urllib3 Cookie Header Leakage
- **CVSS Score:** 8.1 (HIGH, v3.1)
- **Affected Library:** urllib3
- **Affected Version:** 1.26.16
- **Description:** urllib3 does not treat the `Cookie` header specially during HTTP redirects to different origins, potentially leaking sensitive credentials to unintended hosts. Fixed in 1.26.17 / 2.0.6.

### CVE-2022-42969 — py Library ReDoS
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** py
- **Affected Version:** 1.11.0
- **Description:** The `py` library's handling of Subversion repository info data exhibits catastrophic backtracking, allowing denial of service via a crafted SVN repo.

### CVE-2024-3651 — idna Quadratic Complexity DoS
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** idna
- **Affected Version:** 3.6
- **Description:** The `idna.encode()` function processes specially crafted inputs with quadratic complexity, enabling denial of service via excessive CPU consumption. Fixed in 3.7.

### CVE-2022-31116 — ujson Surrogate Character Mishandling
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** UltraJSON (ujson)
- **Affected Version:** 5.3.0
- **Description:** Improper decoding of escaped surrogate characters can corrupt strings and cause key confusion and value overwriting in dictionaries. Fixed in 5.4.0.

### CVE-2021-33503 — urllib3 Authority ReDoS
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** urllib3
- **Affected Version:** 1.26.4
- **Description:** The authority regular expression in urllib3 exhibits catastrophic backtracking when processing URLs with many `@` characters, enabling denial of service. Fixed in 1.26.5.

### CVE-2021-43818 — lxml HTML Cleaner XSS Bypass
- **CVSS Score:** 7.1 (HIGH, v3.1)
- **Affected Library:** lxml
- **Affected Version:** 4.6.4
- **Description:** lxml's HTML Cleaner allows certain crafted `<script>` content and data-URI embedded SVG scripts to pass through the sanitiser. Fixed in 4.6.5.

---

## Summary Table

| CVE ID | CVSS Score | Severity | Affected Library | Affected Version | Base Image |
|---|---|---|---|---|---|
| CVE-2020-14343 | 9.8 | Critical | PyYAML | 5.3.1 | python:3.11-alpine |
| CVE-2021-34552 | 9.8 | Critical | Pillow | 8.2.0 | python:3.11-alpine |
| CVE-2022-37454 | 9.8 | Critical | pysha3 | 1.0.2 | python:3.11-alpine |
| CVE-2019-13132 | 9.8 | Critical | pyzmq | 18.0.2 | python:3.11-alpine |
| CVE-2021-3177 | 9.8 | Critical | Python (CPython) | 3.9.1 | python:3.9.1-alpine3.12 |
| CVE-2022-24303 | 9.1 | Critical | Pillow | 9.0.0 | python:3.11-alpine |
| CVE-2023-43804 | 8.1 | High | urllib3 | 1.26.16 | python:3.11-alpine |
| CVE-2022-42969 | 7.5 | High | py | 1.11.0 | python:3.11-alpine |
| CVE-2024-3651 | 7.5 | High | idna | 3.6 | python:3.11-alpine |
| CVE-2022-31116 | 7.5 | High | ujson | 5.3.0 | python:3.11-alpine |
| CVE-2021-33503 | 7.5 | High | urllib3 | 1.26.4 | python:3.11-alpine |
| CVE-2021-43818 | 7.1 | High | lxml | 4.6.4 | python:3.11-alpine |

**Note — CVE-2021-3177:** This vulnerability is in the CPython runtime itself rather than a pip-installable package. It requires a non-standard base image (`python:3.9.1-alpine3.12`) pinned to a vulnerable Python patch version. A separate baseline container `base-python3.9.1-alpine3.12` is provided for this test case.
