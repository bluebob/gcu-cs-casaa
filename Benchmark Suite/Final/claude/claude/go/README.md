# Go Vulnerability Test Set

## Vulnerabilities

### CVE-2023-49569 — go-git Path Traversal / RCE
- **CVSS Score:** 9.8 (CRITICAL, v3.1)
- **Affected Library:** github.com/go-git/go-git/v5
- **Affected Version:** v5.10.1
- **Description:** A path traversal flaw in go-git allows attackers to create and amend files across the filesystem, potentially achieving remote code execution when using the default ChrootOS filesystem. Fixed in v5.11.0.

### CVE-2021-3121 — gogo/protobuf Array Index Validation
- **CVSS Score:** 8.6 (HIGH, v3.1)
- **Affected Library:** github.com/gogo/protobuf
- **Affected Version:** v1.3.1
- **Description:** Insufficient array index validation in the unmarshal component allows denial of service or potential memory corruption via malformed protocol buffer messages. Fixed in v1.3.2.

### CVE-2022-29153 — HashiCorp Consul SSRF
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** github.com/hashicorp/consul/api
- **Affected Version:** v1.11.3
- **Description:** The Consul client agent follows HTTP redirects from health check endpoints, enabling server-side request forgery attacks. Fixed in v1.11.5.

### CVE-2022-28948 — gopkg.in/yaml.v3 Crash on Unmarshal
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** gopkg.in/yaml.v3
- **Affected Version:** v3.0.0
- **Description:** The Unmarshal function crashes when processing malformed input, enabling denial of service conditions. Fixed in v3.0.1.

### CVE-2022-32149 — golang.org/x/text ParseAcceptLanguage DoS
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** golang.org/x/text
- **Affected Version:** v0.3.7
- **Description:** A crafted Accept-Language header causes significant parsing delays in ParseAcceptLanguage, enabling denial of service. Fixed in v0.3.8.

### CVE-2022-41723 — golang.org/x/net HPACK CPU Exhaustion
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** golang.org/x/net
- **Affected Version:** v0.6.0
- **Description:** A maliciously crafted HTTP/2 stream causes excessive CPU consumption in the HPACK decoder, enabling denial of service from a small number of requests. Fixed in v0.7.0.

### CVE-2023-44487 — HTTP/2 Rapid Reset (golang.org/x/net)
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** golang.org/x/net
- **Affected Version:** v0.16.0
- **Description:** HTTP/2 protocol allows denial of service via rapid stream cancellation (Rapid Reset Attack), actively exploited in the wild. Fixed in v0.17.0.

### CVE-2020-26160 — jwt-go Audience Validation Bypass
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** github.com/dgrijalva/jwt-go
- **Affected Version:** v3.2.0
- **Description:** Audience validation fails via type assertion when the `aud` claim is a string rather than a slice, allowing authentication bypass in services lacking independent audience verification.

### CVE-2020-27813 — gorilla/websocket Integer Overflow DoS
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** github.com/gorilla/websocket
- **Affected Version:** v1.4.0
- **Description:** An integer overflow in WebSocket frame length handling allows remote attackers to trigger denial of service on HTTP servers. Fixed in v1.4.1.

### CVE-2021-27918 — Go encoding/xml Infinite Loop
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** Go standard library (encoding/xml)
- **Affected Version:** Go 1.15.8
- **Description:** encoding/xml enters an infinite loop if a custom TokenReader returns EOF in the middle of an element. Fixed in Go 1.15.9 / 1.16.1.
- **Note:** Requires non-standard base image `golang:1.15.8-alpine3.13`.

### CVE-2021-33196 — Go archive/zip Panic
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** Go standard library (archive/zip)
- **Affected Version:** Go 1.16.4
- **Description:** A maliciously crafted file count in a ZIP archive header triggers a panic in NewReader / OpenReader, enabling denial of service. Fixed in Go 1.16.5.
- **Note:** Requires non-standard base image `golang:1.16.4-alpine3.13`.

### CVE-2021-44716 — Go net/http Memory Exhaustion
- **CVSS Score:** 7.5 (HIGH, v3.1)
- **Affected Library:** Go standard library (net/http)
- **Affected Version:** Go 1.17.4
- **Description:** Malicious HTTP/2 requests cause uncontrolled memory consumption via the header canonicalization cache, enabling denial of service. Fixed in Go 1.17.5.
- **Note:** Requires non-standard base image `golang:1.17.4-alpine3.14`.

---

## Summary Table

| CVE ID | CVSS Score | Severity | Affected Library | Affected Version | Base Image |
|---|---|---|---|---|---|
| CVE-2023-49569 | 9.8 | Critical | go-git/go-git/v5 | v5.10.1 | golang:1.21-alpine |
| CVE-2021-3121 | 8.6 | High | gogo/protobuf | v1.3.1 | golang:1.21-alpine |
| CVE-2022-29153 | 7.5 | High | hashicorp/consul/api | v1.11.3 | golang:1.21-alpine |
| CVE-2022-28948 | 7.5 | High | gopkg.in/yaml.v3 | v3.0.0 | golang:1.21-alpine |
| CVE-2022-32149 | 7.5 | High | golang.org/x/text | v0.3.7 | golang:1.21-alpine |
| CVE-2022-41723 | 7.5 | High | golang.org/x/net | v0.6.0 | golang:1.21-alpine |
| CVE-2023-44487 | 7.5 | High | golang.org/x/net | v0.16.0 | golang:1.21-alpine |
| CVE-2020-26160 | 7.5 | High | dgrijalva/jwt-go | v3.2.0 | golang:1.21-alpine |
| CVE-2020-27813 | 7.5 | High | gorilla/websocket | v1.4.0 | golang:1.21-alpine |
| CVE-2021-27918 | 7.5 | High | Go stdlib (encoding/xml) | Go 1.15.8 | golang:1.15.8-alpine3.13 |
| CVE-2021-33196 | 7.5 | High | Go stdlib (archive/zip) | Go 1.16.4 | golang:1.16.4-alpine3.13 |
| CVE-2021-44716 | 7.5 | High | Go stdlib (net/http) | Go 1.17.4 | golang:1.17.4-alpine3.14 |

**Note — CVE-2021-27918, CVE-2021-33196, CVE-2021-44716:** These vulnerabilities are in the Go standard library and require specific older Go runtime base images. Separate baseline containers are provided for each non-standard base.
