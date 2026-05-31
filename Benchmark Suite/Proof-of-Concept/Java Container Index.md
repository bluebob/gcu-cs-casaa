# Java CVE Benchmark Suite

This document provides an index of container images, each containing a specific Common Vulnerability and Exposure (CVE) related to Java. These images are intended for testing and evaluating the effectiveness of container vulnerability scanners.

**Note on CVEs from the MergeBase Article:**

The article "The Top 10 High-Risk Java Vulnerabilities" from MergeBase lists ten CVEs. However, several of these were not specific to Java libraries (e.g., they were related to Windows, PHP, Ruby, or JavaScript). Therefore, this benchmark suite includes containers for the relevant Java CVEs from the article, supplemented with other well-known and critical Java vulnerabilities to provide a more comprehensive benchmark.

## CVE-2021-45046

*   **Description:** A vulnerability in Apache Log4j in versions later than 2.14.1 but before 2.16.0, which in certain non-default configurations could allow for information leak and remote code execution.
*   **Vulnerable Component:** `org.apache.logging.log4j:log4j-core`
*   **Vulnerable Version:** 2.15.0
*   **Dockerfile:** `benchmarks/java/CVE-2021-45046/Dockerfile`
*   **Build Command:** `docker build -t java-cve-2021-45046 .` (run from within the `benchmarks/java/CVE-2021-45046` directory)

## CVE-2017-5638

*   **Description:** A remote code execution vulnerability in Apache Struts 2 that allows an attacker to execute arbitrary commands via a crafted Content-Type header.
*   **Vulnerable Component:** `org.apache.struts:struts2-core`
*   **Vulnerable Version:** 2.5.10
*   **Dockerfile:** `benchmarks/java/CVE-2017-5638/Dockerfile`
*   **Build Command:** `docker build -t java-cve-2017-5638 .` (.run from within the `benchmarks/java/CVE-2017-5638` directory)

## CVE-2022-22947

*   **Description:** A code injection vulnerability in Spring Cloud Gateway that allows an attacker to execute arbitrary code when the Gateway Actuator endpoint is enabled, exposed, and unsecured.
*   **Vulnerable Component:** `org.springframework.cloud:spring-cloud-starter-gateway`
*   **Vulnerable Version:** 3.1.0
*   **Dockerfile:** `benchmarks/java/CVE-2022-22947/Dockerfile`
*   **Build Command:** `docker build -t java-cve-2022-22947 .` (run from within the `benchmarks/java/CVE-2022-22947` directory)

## CVE-2018-14721

*   **Description:** A deserialization vulnerability in `jackson-databind` that can allow an attacker to execute arbitrary code.
*   **Vulnerable Component:** `com.fasterxml.jackson.core:jackson-databind`
*   **Vulnerable Version:** 2.9.6
*   **Dockerfile:** `benchmarks/java/CVE-2018-14721/Dockerfile`
*   **Build Command:** `docker build -t java-cve-2018-14721 .` (run from within the `benchmarks/java/CVE-2018-14721` directory)

## CVE-2016-1000031

*   **Description:** A remote code execution vulnerability in the Spring Framework.
*   **Vulnerable Component:** `org.springframework:spring-webmvc`
*   **Vulnerable Version:** 4.3.2.RELEASE
*   **Dockerfile:** `benchmarks/java/CVE-2016-1000031/Dockerfile`
*   **Build Command:** `docker build -t java-cve-2016-1000031 .` (run from within the `benchmarks/java/CVE-2016-1000031` directory)

## CVE-2022-22965 (Spring4Shell)

*   **Description:** A remote code execution vulnerability in the Spring Framework that affects Spring MVC and Spring WebFlux applications running on JDK 9+.
*   **Vulnerable Component:** `org.springframework:spring-webmvc`
*   **Vulnerable Version:** 5.3.17
*   **Dockerfile:** `benchmarks/java/CVE-2022-22965/Dockerfile`
*   **Build Command:** `docker build -t java-cve-2022-22965 .` (run from within the `benchmarks/java/CVE-2022-22965` directory)

## CVE-2017-12629

*   **Description:** A remote code execution vulnerability in Apache Solr.
*   **Vulnerable Component:** `org.apache.solr:solr-core`
*   **Vulnerable Version:** 7.0.0
*   **Dockerfile:** `benchmarks/java/CVE-2017-12629/Dockerfile`
*   **Build Command:** `docker build -t java-cve-2017-12629 .` (run from within the `benchmarks/java/CVE-2017-12629` directory)

## CVE-2018-11776

*   **Description:** A remote code execution vulnerability in Apache Struts 2.
*   **Vulnerable Component:** `org.apache.struts:struts2-core`
*   **Vulnerable Version:** 2.5.16
*   **Dockerfile:** `benchmarks/java/CVE-2018-11776/Dockerfile`
*   **Build Command:** `docker build -t java-cve-2018-11776 .` (run from within the `benchmarks/java/CVE-2018-11776` directory)
