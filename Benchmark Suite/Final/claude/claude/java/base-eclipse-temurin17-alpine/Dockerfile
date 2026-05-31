FROM --platform=linux/amd64 eclipse-temurin:17-alpine
# Baseline container — no application vulnerabilities
# Used to establish base image CVE baseline for scanner result normalisation
COPY App.java .
RUN javac App.java
CMD ["java", "App"]
