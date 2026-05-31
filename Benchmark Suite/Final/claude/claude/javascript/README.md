# JavaScript Vulnerability Test Set

## Vulnerabilities

### CVE-2021-3918 — json-schema Prototype Pollution
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** json-schema
- **Affected Version:** 0.3.0
- **Description:** The json-schema library allows improperly controlled modification of Object prototype attributes, enabling prototype pollution that can lead to remote code execution. Fixed in 0.4.0.

### CVE-2022-37601 — loader-utils Prototype Pollution
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** loader-utils
- **Affected Version:** 2.0.2
- **Description:** A prototype pollution flaw in the parseQuery function allows attackers to modify object properties and compromise application integrity. Fixed in 2.0.3.

### CVE-2021-44906 — minimist Prototype Pollution
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** minimist
- **Affected Version:** 1.2.5
- **Description:** The setKey() function allows prototype pollution through crafted arguments, enabling unauthorized modification of application behaviour. Fixed in 1.2.6.

### CVE-2019-10744 — lodash Prototype Pollution
- **CVSS Score:** 9.1 (CRITICAL, v3.1)
- **Affected Library:** lodash
- **Affected Version:** 4.17.11
- **Description:** The defaultsDeep function allows attackers to exploit prototype pollution via constructor payloads, adding or modifying Object.prototype properties. Fixed in 4.17.12.

### CVE-2022-46175 — json5 Prototype Pollution
- **CVSS Score:** 8.8 (HIGH, v3.1)
- **Affected Library:** json5
- **Affected Version:** 2.2.1
- **Description:** The JSON5 parse method fails to restrict `__proto__` keys, permitting prototype pollution that can enable denial of service, XSS, or remote code execution. Fixed in 2.2.2.

### CVE-2022-24999 — qs Prototype Pollution / DoS
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** qs
- **Affected Version:** 6.10.2
- **Description:** A prototype pollution vulnerability allows attackers to hang Node.js processes by exploiting the `__proto__` key in query strings. Fixed in 6.10.3.

### CVE-2022-31129 — moment ReDoS
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** moment
- **Affected Version:** 2.29.3
- **Description:** An inefficient parsing algorithm with quadratic complexity enables denial of service when processing overly long date strings. Fixed in 2.29.4.

### CVE-2021-27290 — ssri ReDoS
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** ssri
- **Affected Version:** 8.0.0
- **Description:** A ReDoS vulnerability allows malicious SRI strings to consume excessive CPU time when strict validation is enabled. Fixed in 8.0.1.

### CVE-2022-25881 — http-cache-semantics ReDoS
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** http-cache-semantics
- **Affected Version:** 4.1.0
- **Description:** Malicious request headers to servers using this library for cache policy parsing can trigger ReDoS. Fixed in 4.1.1.

### CVE-2022-38900 — decode-uri-component Input Validation DoS
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** decode-uri-component
- **Affected Version:** 0.2.0
- **Description:** Improper input validation allows denial of service via malformed URI components. Fixed in 0.2.1.

### CVE-2021-23337 — lodash Command Injection
- **CVSS Score:** 7.2 (HIGH, v3.1)
- **Affected Library:** lodash
- **Affected Version:** 4.17.20
- **Description:** The template function allows privileged attackers to execute arbitrary commands through code injection. Fixed in 4.17.21.

### CVE-2021-23358 — underscore.js Template Injection
- **CVSS Score:** 7.2 (HIGH, v3.1)
- **Affected Library:** underscore
- **Affected Version:** 1.12.0
- **Description:** The template function fails to sanitise variable properties, allowing attackers to inject arbitrary code through unsanitised template variables. Fixed in 1.13.0-2.

---

## Summary Table

| CVE ID | CVSS Score | Severity | Affected Library | Affected Version | Base Image |
|---|---|---|---|---|---|
| CVE-2021-3918 | 9.8 | Critical | json-schema | 0.3.0 | node:20-alpine |
| CVE-2022-37601 | 9.8 | Critical | loader-utils | 2.0.2 | node:20-alpine |
| CVE-2021-44906 | 9.8 | Critical | minimist | 1.2.5 | node:20-alpine |
| CVE-2019-10744 | 9.1 | Critical | lodash | 4.17.11 | node:20-alpine |
| CVE-2022-46175 | 8.8 | High | json5 | 2.2.1 | node:20-alpine |
| CVE-2022-24999 | 7.5 | High | qs | 6.10.2 | node:20-alpine |
| CVE-2022-31129 | 7.5 | High | moment | 2.29.3 | node:20-alpine |
| CVE-2021-27290 | 7.5 | High | ssri | 8.0.0 | node:20-alpine |
| CVE-2022-25881 | 7.5 | High | http-cache-semantics | 4.1.0 | node:20-alpine |
| CVE-2022-38900 | 7.5 | High | decode-uri-component | 0.2.0 | node:20-alpine |
| CVE-2021-23337 | 7.2 | High | lodash | 4.17.20 | node:20-alpine |
| CVE-2021-23358 | 7.2 | High | underscore | 1.12.0 | node:20-alpine |
