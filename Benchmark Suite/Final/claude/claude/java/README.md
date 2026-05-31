# Java Vulnerability Test Set

## Vulnerabilities

### CVE-2021-44228 — Log4Shell (Apache Log4j2 RCE)
- **CVSS Score:** 10.0 (CRITICAL, v3.1)
- **Affected Library:** org.apache.logging.log4j:log4j-core
- **Affected Version:** 2.14.1
- **Description:** Log4j2's JNDI lookup feature allows attackers who control log message content to execute arbitrary code loaded from remote LDAP servers. Fixed in 2.16.0.

### CVE-2022-22947 — Spring Cloud Gateway RCE
- **CVSS Score:** 10.0 (CRITICAL, v3.1)
- **Affected Library:** org.springframework.cloud:spring-cloud-gateway-core
- **Affected Version:** 3.1.0
- **Description:** A code injection vulnerability in Spring Cloud Gateway's routing feature allows remote arbitrary code execution via malicious SpEL expressions when the Actuator endpoint is exposed. Fixed in 3.1.1.

### CVE-2022-22965 — Spring4Shell (Spring Framework RCE)
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** org.springframework:spring-webmvc
- **Affected Version:** 5.3.17
- **Description:** Spring MVC applications on JDK 9+ are vulnerable to remote code execution through data binding when deployed as a WAR on Tomcat. Fixed in 5.3.18.

### CVE-2017-5638 — Apache Struts Jakarta Multipart RCE
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** org.apache.struts:struts2-core
- **Affected Version:** 2.3.31
- **Description:** Improper exception handling in the Jakarta Multipart parser allows remote code execution via crafted Content-Type headers (used in the Equifax breach). Fixed in 2.3.32.

### CVE-2022-22963 — Spring Cloud Function SpEL RCE
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** org.springframework.cloud:spring-cloud-function-context
- **Affected Version:** 3.2.2
- **Description:** The routing expression feature executes arbitrary SpEL expressions from HTTP request headers, enabling unauthenticated remote code execution. Fixed in 3.2.3.

### CVE-2022-42889 — Text4Shell (Apache Commons Text RCE)
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** org.apache.commons:commons-text
- **Affected Version:** 1.9
- **Description:** The variable interpolation feature enables dangerous lookups including script execution and remote URL loading by default, allowing remote code execution on untrusted input. Fixed in 1.10.0.

### CVE-2020-1938 — Ghostcat (Apache Tomcat AJP File Read/RCE)
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** org.apache.tomcat.embed:tomcat-embed-core
- **Affected Version:** 9.0.30
- **Description:** The AJP connector in Tomcat allows unauthenticated retrieval of arbitrary files and JSP execution when the AJP port is accessible. Fixed in 9.0.31.

### CVE-2019-17571 — Apache Log4j 1.x Deserialization RCE
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** log4j:log4j
- **Affected Version:** 1.2.17
- **Description:** The SocketServer class deserializes untrusted data, enabling remote code execution via deserialization gadget chains. This is the final release of the unmaintained Log4j 1.x branch.

### CVE-2021-31805 — Apache Struts OGNL Double Evaluation RCE
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** org.apache.struts:struts2-core
- **Affected Version:** 2.5.29
- **Description:** Incomplete fix for a prior vulnerability leaves certain tag attributes susceptible to double OGNL evaluation, enabling remote code execution. Fixed in 2.5.30.

### CVE-2016-4437 — Apache Shiro RememberMe Deserialization RCE
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** org.apache.shiro:shiro-core
- **Affected Version:** 1.2.4
- **Description:** When no cipher key is configured for the RememberMe cookie, attackers can execute arbitrary code by sending a crafted cookie exploiting Java deserialization. Fixed in 1.2.5.

### CVE-2021-45046 — Log4j2 JNDI RCE (incomplete fix)
- **CVSS Score:** 9.0 (CRITICAL, v3.1)
- **Affected Library:** org.apache.logging.log4j:log4j-core
- **Affected Version:** 2.15.0
- **Description:** The fix for CVE-2021-44228 was incomplete in non-default configurations; Thread Context Map data combined with certain patterns could still enable information leak and remote code execution. Fixed in 2.16.0.

### CVE-2020-36518 — Jackson-databind Stack Overflow DoS
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** com.fasterxml.jackson.core:jackson-databind
- **Affected Version:** 2.13.2
- **Description:** Deeply nested JSON objects cause a stack overflow exception in jackson-databind's deserialization, enabling denial of service. Fixed in 2.13.2.1.

---

## Summary Table

| CVE ID | CVSS Score | Severity | Affected Library | Affected Version | Base Image |
|---|---|---|---|---|---|
| CVE-2021-44228 | 10.0 | Critical | log4j-core | 2.14.1 | eclipse-temurin:17-alpine |
| CVE-2022-22947 | 10.0 | Critical | spring-cloud-gateway-core | 3.1.0 | eclipse-temurin:17-alpine |
| CVE-2022-22965 | 9.8 | Critical | spring-webmvc | 5.3.17 | eclipse-temurin:17-alpine |
| CVE-2017-5638 | 9.8 | Critical | struts2-core | 2.3.31 | eclipse-temurin:17-alpine |
| CVE-2022-22963 | 9.8 | Critical | spring-cloud-function-context | 3.2.2 | eclipse-temurin:17-alpine |
| CVE-2022-42889 | 9.8 | Critical | commons-text | 1.9 | eclipse-temurin:17-alpine |
| CVE-2020-1938 | 9.8 | Critical | tomcat-embed-core | 9.0.30 | eclipse-temurin:17-alpine |
| CVE-2019-17571 | 9.8 | Critical | log4j | 1.2.17 | eclipse-temurin:17-alpine |
| CVE-2021-31805 | 9.8 | Critical | struts2-core | 2.5.29 | eclipse-temurin:17-alpine |
| CVE-2016-4437 | 9.8 | Critical | shiro-core | 1.2.4 | eclipse-temurin:17-alpine |
| CVE-2021-45046 | 9.0 | Critical | log4j-core | 2.15.0 | eclipse-temurin:17-alpine |
| CVE-2020-36518 | 7.5 | High | jackson-databind | 2.13.2 | eclipse-temurin:17-alpine |
