FROM --platform=linux/amd64 alpine:3.19
# Baseline container — no application vulnerabilities
# Used to establish base image CVE baseline for scanner result normalisation
RUN apk add --no-cache g++
COPY app.cpp .
RUN g++ -o app app.cpp
CMD ["./app"]
