# Build stage
FROM maven:3.6.3-jdk-8 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package

# Package stage
FROM openjdk:8-jre-slim
WORKDIR /app
COPY --from=build /app/target/vulnerable-app-1.0-SNAPSHOT.jar .
LABEL cve="CVE-2021-44228"
LABEL library="log4j-core"
LABEL version="2.14.1"
CMD ["java", "-jar", "vulnerable-app-1.0-SNAPSHOT.jar"]
