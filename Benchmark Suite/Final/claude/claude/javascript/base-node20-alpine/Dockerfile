FROM --platform=linux/amd64 node:20-alpine
# Baseline container — no application vulnerabilities
# Used to establish base image CVE baseline for scanner result normalisation
COPY app.js .
CMD ["node", "app.js"]
