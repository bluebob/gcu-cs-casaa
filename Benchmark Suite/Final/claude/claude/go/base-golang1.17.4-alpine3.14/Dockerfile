FROM --platform=linux/amd64 golang:1.17.4-alpine3.14
# Baseline container — no application vulnerabilities
# Used to establish base image CVE baseline for scanner result normalisation
COPY app.go .
CMD ["go", "run", "app.go"]
