FROM --platform=linux/amd64 golang:1.21-alpine
# Baseline container — no application vulnerabilities
# Used to establish base image CVE baseline for scanner result normalisation
COPY app.go .
RUN go run app.go
CMD ["go", "run", "app.go"]
