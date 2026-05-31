FROM --platform=linux/amd64 python:3.11-alpine
# Baseline container — no application vulnerabilities
# Used to establish base image CVE baseline for scanner result normalisation
COPY app.py .
CMD ["python", "app.py"]
