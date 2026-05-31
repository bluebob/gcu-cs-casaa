# Go CVE Benchmark Suite

This document provides an index of container images, each containing a specific Common Vulnerability and Exposure (CVE) related to the Go language and its libraries. These images are intended for testing and evaluating the effectiveness of container vulnerability scanners.

## CVE-2023-44487

*   **Description:** HTTP/2 Rapid Reset Attack. The HTTP/2 protocol allows a denial of service (server resource consumption) because request cancellation can reset many streams quickly.
*   **Vulnerable Component:** `net/http`
*   **Vulnerable Version:** Go 1.21.2
*   **Dockerfile:** `benchmarks/go/CVE-2023-44487/Dockerfile`
*   **Build Command:** `docker build -t go-cve-2023-44487 .` (run from within the `benchmarks/go/CVE-2023-44487` directory)

## CVE-2023-58187

*   **Description:** `crypto/x509` Certificate Chain Validation Denial of Service.
*   **Vulnerable Component:** `crypto/x509`
*   **Vulnerable Version:** Go 1.21.3
*   **Dockerfile:** `benchmarks/go/CVE-2023-58187/Dockerfile`
*   **Build Command:** `docker build -t go-cve-2023-58187 .` (run from within the `benchmarks/go/CVE-2023-58187` directory)

## CVE-2018-16875

*   **Description:** `crypto/x509` Package CPU Denial of Service.
*   **Vulnerable Component:** `crypto/x509`
*   **Vulnerable Version:** Go 1.11.2
*   **Dockerfile:** `benchmarks/go/CVE-2018-16875/Dockerfile`
*   **Build Command:** `docker build -t go-cve-2018-16875 .` (run from within the `benchmarks/go/CVE-2018-16875` directory)

## CVE-2023-29406

*   **Description:** HTTP/1 Client Host Header Injection.
*   **Vulnerable Component:** `net/http`
*   **Vulnerable Version:** Go 1.19
*   **Dockerfile:** `benchmarks/go/CVE-2023-29406/Dockerfile`
*   **Build Command:** `docker build -t go-cve-2023-29406 .` (run from within the `benchmarks/go/CVE-2023-29406` directory)

## CVE-2020-29652

*   **Description:** A vulnerability in `github.com/gin-gonic/gin` affecting the `httputil.ReverseProxy`.
*   **Vulnerable Component:** `github.com/gin-gonic/gin`
*   **Vulnerable Version:** v1.6.3
*   **Dockerfile:** `benchmarks/go/CVE-2020-29652/Dockerfile`
*   **Build Command:** `docker build -t go-cve-2020-29652 .` (run from within the `benchmarks/go/CVE-2020-29652` directory)

## CVE-2022-27664

*   **Description:** A heap overflow in `golang.org/x/net/http2/h2c`.
*   **Vulnerable Component:** `golang.org/x/net`
*   **Vulnerable Version:** v0.0.0-20220920224401-6433c02018a6
*   **Dockerfile:** `benchmarks/go/CVE-2022-27664/Dockerfile`
*   **Build Command:** `docker build -t go-cve-2022-27664 .` (run from within the `benchmarks/go/CVE-2022-27664` directory)

## CVE-2022-32149

*   **Description:** A denial of service vulnerability in `golang.org/x/text`.
*   **Vulnerable Component:** `golang.org/x/text`
*   **Vulnerable Version:** v0.3.7
*   **Dockerfile:** `benchmarks/go/CVE-2022-32149/Dockerfile`
*   **Build Command:** `docker build -t go-cve-2022-32149 .` (run from within the `benchmarks/go/CVE-2022-32149` directory)

## CVE-2022-41717

*   **Description:** A denial of service vulnerability in `net/http` due to excessive memory allocation.
*   **Vulnerable Component:** `net/http`
*   **Vulnerable Version:** Go 1.19.2
*   **Dockerfile:** `benchmarks/go/CVE-2022-41717/Dockerfile`
*   **Build Command:** `docker build -t go-cve-2022-41717 .` (run from within the `benchmarks/go/CVE-2022-41717` directory)

## CVE-2021-3121

*   **Description:** A denial of service vulnerability in `gopkg.in/yaml.v2`.
*   **Vulnerable Component:** `gopkg.in/yaml.v2`
*   **Vulnerable Version:** v2.2.7
*   **Dockerfile:** `benchmarks/go/CVE-2021-3121/Dockerfile`
*   **Build Command:** `docker build -t go-cve-2021-3121 .` (run from within the `benchmarks/go/CVE-2021-3121` directory)

## CVE-2021-44716

*   **Description:** A vulnerability in the Go standard library's `net/http/httputil` `ReverseProxy`.
*   **Vulnerable Component:** `net/http/httputil`
*   **Vulnerable Version:** Go 1.17.8
*   **Dockerfile:** `benchmarks/go/CVE-2021-44716/Dockerfile`
*   **Build Command:** `docker build -t go-cve-2021-44716 .` (run from within the `benchmarks/go/CVE-2021-44716` directory)
