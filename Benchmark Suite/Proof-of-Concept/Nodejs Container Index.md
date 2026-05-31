# Node.js CVE Benchmark Suite

This document provides an index of container images, each containing a specific Common Vulnerability and Exposure (CVE) related to Node.js. These images are intended for testing and evaluating the effectiveness of container vulnerability scanners.

**Note on CVEs from the HeroDevs Article:**

The article "Top 10 Critical CVEs in End-of-Life Node.js Versions" from HeroDevs lists ten CVEs. However, the first six CVEs listed in the article appear to have incorrect identifiers (e.g., using the year 2025) and could not be reliably verified against the National Vulnerability Database (NVD). Therefore, this benchmark suite only includes containers for the four CVEs that could be positively identified.

## CVE-2021-22918

*   **Description:** Use After Free in HTTP2 on Stream Canceling.
*   **Vulnerable Component:** Node.js
*   **Vulnerable Version:** 14.17.0
*   **Dockerfile:** `benchmarks/nodejs/CVE-2021-22918/Dockerfile`
*   **Build Command:** `docker build -t nodejs-cve-2021-22918 .` (run from within the `benchmarks/nodejs/CVE-2021-22918` directory)

## CVE-2021-22921

*   **Description:** DNS Rebinding in --inspect via Invalid Host Headers.
*   **Vulnerable Component:** Node.js
*   **Vulnerable Version:** 16.2.0
*   **Dockerfile:** `benchmarks/nodejs/CVE-2021-22921/Dockerfile`
*   **Build Command:** `docker build -t nodejs-cve-2021-22921 .` (run from within the `benchmarks/nodejs/CVE-2021-22921` directory)

## CVE-2021-22930

*   **Description:** Weak Random Number Generation in Crypto Module.
*   **Vulnerable Component:** Node.js
*   **Vulnerable Version:** 16.6.1
*   **Dockerfile:** `benchmarks/nodejs/CVE-2021-22930/Dockerfile`
*   **Build Command:** `docker build -t nodejs-cve-2021-22930 .` (run from within the `benchmarks/nodejs/CVE-2021-22930` directory)

## CVE-2021-22931

*   **Description:** HTTP Request Smuggling via Malformed Transfer-Encoding Header.
*   **Vulnerable Component:** Node.js
*   **Vulnerable Version:** 16.4.0
*   **Dockerfile:** `benchmarks/nodejs/CVE-2021-22931/Dockerfile`
*   **Build Command:** `docker build -t nodejs-cve-2021-22931 .` (run from within the `benchmarks/nodejs/CVE-2021-22931` directory)
