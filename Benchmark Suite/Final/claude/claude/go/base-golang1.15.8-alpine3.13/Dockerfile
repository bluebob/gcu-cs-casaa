FROM --platform=linux/amd64 golang:1.15.8-alpine3.13
# Baseline container — no application vulnerabilities
# Used to establish base image CVE baseline for scanner result normalisation
COPY app.go .
CMD ["go", "run", "app.go"]
