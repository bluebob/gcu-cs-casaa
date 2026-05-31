# C++ Vulnerability Test Set

## Vulnerabilities

### CVE-2021-3711 — OpenSSL SM2 Decryption Buffer Overflow
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** OpenSSL
- **Affected Version:** 1.1.1k
- **Description:** A buffer overflow in the SM2 decryption code occurs because the buffer size calculation for the decrypted plaintext can be smaller than the actual required size, allowing up to 62 bytes of overflow. Fixed in 1.1.1l.

### CVE-2023-38545 — libcurl SOCKS5 Heap Buffer Overflow
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** curl (libcurl)
- **Affected Version:** 7.88.0
- **Description:** A heap buffer overflow in the SOCKS5 proxy handshake occurs when processing hostnames exceeding 255 bytes, potentially enabling memory corruption. Fixed in 8.4.0.

### CVE-2022-37434 — zlib Heap Buffer Overflow in inflate
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** zlib
- **Affected Version:** 1.2.12
- **Description:** A heap-based buffer overflow in zlib's inflate function occurs when processing gzip headers with excessively large extra fields in applications calling inflateGetHeader. Fixed in 1.2.13.

### CVE-2022-25235 — Expat XML Parser UTF-8 Validation Flaw
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** expat (libexpat)
- **Affected Version:** 2.4.4
- **Description:** The xmltok_impl.c component lacks proper validation of UTF-8 character encoding in certain XML parsing contexts, creating a critical vulnerability. Fixed in 2.4.5.

### CVE-2021-3520 — lz4 Integer Overflow Out-of-Bounds Write
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** lz4
- **Affected Version:** 1.9.3
- **Description:** An integer overflow in lz4 allows out-of-bounds writes via a crafted file, potentially causing application crashes and data corruption. Fixed in 1.9.4.

### CVE-2019-12900 — bzip2 Out-of-Bounds Write
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** bzip2
- **Affected Version:** 1.0.6
- **Description:** An out-of-bounds write exists in BZ2_decompress when processing files with an excessive number of selectors. Fixed in 1.0.7.

### CVE-2022-1586 — PCRE2 Out-of-Bounds Read
- **CVSS Score:** 9.1 (CRITICAL, v3.1)
- **Affected Library:** pcre2
- **Affected Version:** 10.39
- **Description:** An out-of-bounds read in compile_xclass_matchingpath() affects unicode property matching in JIT-compiled regular expressions during case-less matching. Fixed in 10.40.

### CVE-2022-42915 — libcurl Double Free
- **CVSS Score:** 8.1 (HIGH, v3.1)
- **Affected Library:** curl (libcurl)
- **Affected Version:** 7.85.0
- **Description:** A double-free vulnerability occurs when curl uses an HTTP proxy for non-HTTP(S) transfers and the proxy returns a non-200 response code. Fixed in 7.86.0.

### CVE-2022-3602 — OpenSSL X.509 Name Constraint Buffer Overflow
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** OpenSSL
- **Affected Version:** 3.0.6
- **Description:** A buffer overflow in X.509 name constraint checking can cause denial of service or potentially code execution when processing malicious email addresses in certificates. Fixed in 3.0.7.

### CVE-2022-0778 — OpenSSL BN_mod_sqrt Infinite Loop
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** OpenSSL
- **Affected Version:** 1.1.1m
- **Description:** A bug in BN_mod_sqrt() causes infinite loops when parsing certificates with invalid elliptic curve parameters, enabling denial of service. Fixed in 1.1.1n.

### CVE-2023-0286 — OpenSSL X.400 Type Confusion
- **CVSS Score:** 7.4 (HIGH, v3.1)
- **Affected Library:** OpenSSL
- **Affected Version:** 1.1.1s
- **Description:** A type confusion flaw in X.400 address handling in X.509 certificates can enable information disclosure or denial of service when CRL validation is enabled. Fixed in 1.1.1t.

### CVE-2022-3786 — OpenSSL X.509 Email Address Buffer Overflow
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** OpenSSL
- **Affected Version:** 3.0.6
- **Description:** A buffer overflow in X.509 name constraint checking via malicious email addresses in punycode can result in denial of service; both this and CVE-2022-3602 affect the same library version. Fixed in 3.0.7.

---

## Summary Table

| CVE ID | CVSS Score | Severity | Affected Library | Affected Version | Base Image |
|---|---|---|---|---|---|
| CVE-2021-3711 | 9.8 | Critical | openssl | 1.1.1k | alpine:3.19 |
| CVE-2023-38545 | 9.8 | Critical | curl | 7.88.0 | alpine:3.19 |
| CVE-2022-37434 | 9.8 | Critical | zlib | 1.2.12 | alpine:3.19 |
| CVE-2022-25235 | 9.8 | Critical | expat | 2.4.4 | alpine:3.19 |
| CVE-2021-3520 | 9.8 | Critical | lz4 | 1.9.3 | alpine:3.19 |
| CVE-2019-12900 | 9.8 | Critical | bzip2 | 1.0.6 | alpine:3.19 |
| CVE-2022-1586 | 9.1 | Critical | pcre2 | 10.39 | alpine:3.19 |
| CVE-2022-42915 | 8.1 | High | curl | 7.85.0 | alpine:3.19 |
| CVE-2022-3602 | 7.5 | High | openssl | 3.0.6 | alpine:3.19 |
| CVE-2022-0778 | 7.5 | High | openssl | 1.1.1m | alpine:3.19 |
| CVE-2023-0286 | 7.4 | High | openssl | 1.1.1s | alpine:3.19 |
| CVE-2022-3786 | 7.5 | High | openssl | 3.0.6 | alpine:3.19 |

**Note — C++ package manager:**

All test cases use a multi-stage Docker build: a builder stage compiles the vulnerable library from the upstream source tarball and links the C++ test app against it; the final stage is a clean `alpine:3.19` image containing only the shared library and the app binary. The vulnerable library is installed to `/usr/local/lib` and exposed via `LD_LIBRARY_PATH`. Scanners that inspect ELF binaries for embedded version strings (e.g., Trivy) will detect these vulnerabilities.

| Test case | Source tarball |
|---|---|
| CVE-2021-3711 | openssl 1.1.1k — GitHub releases (`OpenSSL_1_1_1k`) |
| CVE-2022-0778 | openssl 1.1.1m — GitHub releases (`OpenSSL_1_1_1m`) |
| CVE-2022-3602 | openssl 3.0.6 — GitHub archive (`openssl-3.0.6`) |
| CVE-2022-3786 | openssl 3.0.6 — GitHub archive (`openssl-3.0.6`) |
| CVE-2023-0286 | openssl 1.1.1s — GitHub releases (`OpenSSL_1_1_1s`) |
| CVE-2019-12900 | bzip2 1.0.6 — sourceware.org |
| CVE-2021-3520 | lz4 1.9.3 — GitHub archive (`v1.9.3`) |
| CVE-2022-37434 | zlib 1.2.12 — zlib.net fossils |
| CVE-2022-1586 | pcre2 10.39 — GitHub releases |
| CVE-2022-25235 | expat 2.4.4 — GitHub releases (`R_2_4_4`) |
| CVE-2022-42915 | curl 7.85.0 — GitHub releases (`curl-7_85_0`) |
| CVE-2023-38545 | curl 7.88.0 — GitHub releases (`curl-7_88_0`) |
