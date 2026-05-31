# Python CVE Benchmark Suite

This document provides an index of container images, each containing a specific Common Vulnerability and Exposure (CVE) related to Python. These images are intended for testing and evaluating the effectiveness of container vulnerability scanners.

## CVE-2022-37454

*   **Description:** Buffer Overflow in _sha3 module. This critical vulnerability (CVSS 9.8) in the Keccak XKCP SHA-3 reference implementation, used by Python's _sha3 module, allowed attackers to potentially execute arbitrary code via an integer overflow and resultant buffer overflow in the sponge function interface.
*   **Vulnerable Component:** Python Standard Library (`_sha3` module)
*   **Vulnerable Version:** Python 3.10.6
*   **Dockerfile:** `benchmarks/python/CVE-2022-37454/Dockerfile`
*   **Build Command:** `docker build -t python-cve-2022-37454 .` (run from within the `benchmarks/python/CVE-2022-37454` directory)

## CVE-2022-28470

*   **Description:** Backdoor in marcador package. The marcador package versions 0.1 through 0.13 included a code-execution backdoor, demonstrating a severe threat from malicious packages in public repositories like PyPI.
*   **Vulnerable Component:** `marcador` package
*   **Vulnerable Version:** 0.13
*   **Dockerfile:** `benchmarks/python/CVE-2022-28470/Dockerfile`
*   **Build Command:** `docker build -t python-cve-2022-28470 .` (run from within the `benchmarks/python/CVE-2022-28470` directory)

## CVE-2022-48565

*   **Description:** An XML External Entity (XXE) issue in the plistlib module allowed entity declarations in XML plist files, which could lead to information disclosure or DoS attacks.
*   **Vulnerable Component:** Python Standard Library (`plistlib` module)
*   **Vulnerable Version:** Python 3.10.8
*   **Dockerfile:** `benchmarks/python/CVE-2022-48565/Dockerfile`
*   **Build Command:** `docker build -t python-cve-2022-48565 .` (run from within the `benchmarks/python/CVE-2022-48565` directory)

## CVE-2023-6597

*   **Description:** Symlink Dereference in tempfile.TemporaryDirectory on Windows. On Windows systems, this vulnerability allowed users running privileged programs to potentially modify permissions of files referenced by symlinks, leading to a local privilege escalation risk.
*   **Vulnerable Component:** Python Standard Library (`tempfile` module)
*   **Note:** This vulnerability is specific to Windows and cannot be reproduced in a Linux container.

## CVE-2022-42919

*   **Description:** Local Privilege Escalation via multiprocessing on Linux. This flaw allowed pickles to be deserialized from any user in the same machine's local network namespace when using the non-default "forkserver" start method, enabling local privilege escalation to the forkserver process owner.
*   **Vulnerable Component:** Python Standard Library (`multiprocessing` module)
*   **Vulnerable Version:** Python 3.10.7
*   **Dockerfile:** `benchmarks/python/CVE-2022-42919/Dockerfile`
*   **Build Command:** `docker build -t python-cve-2022-42919 .` (run from within the `benchmarks/python/CVE-2022-42919` directory)

## CVE-2024-6345

*   **Description:** RCE in setuptools via download functions. This vulnerability in the package_index module of setuptools allowed RCE via its download functions if exposed to user-controlled inputs (e.g., package URLs), fixed in version 70.0.
*   **Vulnerable Component:** `setuptools` package
*   **Vulnerable Version:** 69.0.0
*   **Dockerfile:** `benchmarks/python/CVE-2024-6345/Dockerfile`
*   **Build Command:** `docker build -t python-cve-2024-6345 .` (run from within the `benchmarks/python/CVE-2024-6345` directory)

## CVE-2019-20907

*   **Description:** A denial of service vulnerability where opening a crafted file in the tarfile module could lead to an infinite loop.
*   **Vulnerable Component:** Python Standard Library (`tarfile` module)
*   **Vulnerable Version:** Python 3.7
*   **Dockerfile:** `benchmarks/python/CVE-2019-20907/Dockerfile`
*   **Build Command:** `docker build -t python-cve-2019-20907 .` (run from within the `benchmarks/python/CVE-2019-20907` directory)

## CVE-2024-45061

*   **Description:** DoS via Slow IDNA Decoding. An unnecessary quadratic algorithm in the IDNA decoder path could lead to a CPU denial of service when processing a crafted, long hostname, such as in an HTTP Location header.
*   **Vulnerable Component:** Python Standard Library (`IDNA` decoder)
*   **Vulnerable Version:** Python 3.10.13
*   **Dockerfile:** `benchmarks/python/CVE-2024-45061/Dockerfile`
*   **Build Command:** `docker build -t python-cve-2024-45061 .` (run from within the `benchmarks/python/CVE-2024-45061` directory)

## CVE-2021-3177

*   **Description:** A buffer overflow in the PyCArg_repr function within the ctypes module could be exploited.
*   **Vulnerable Component:** Python Standard Library (`ctypes` module)
*   **Vulnerable Version:** Python 3.9.1
*   **Dockerfile:** `benchmarks/python/CVE-2021-3177/Dockerfile`
*   **Build Command:** `docker build -t python-cve-2021-3177 .` (run from within the `benchmarks/python/CVE-2021-3177` directory)

## CVE-2023-24329

*   **Description:** An issue where urllib.parse allowed attackers to bypass blocklisting methods by supplying a URL that started with blank characters, potentially leading to security control bypasses.
*   **Vulnerable Component:** Python Standard Library (`urllib.parse` module)
*   **Vulnerable Version:** Python 3.10.10
*   **Dockerfile:** `benchmarks/python/CVE-2023-24329/Dockerfile`
*   **Build Command:** `docker build -t python-cve-2023-24329 .` (run from within the `benchmarks/python/CVE-2023-24329` directory)
