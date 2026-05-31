FROM node:16-slim

LABEL cve="CVE-2021-23337"
LABEL library="lodash"
LABEL version="4.17.20"

WORKDIR /app

COPY package.json .

RUN npm install
