FROM node:20-slim

WORKDIR /app

COPY ./service/nodejs/src/package.json /app/

RUN yarn install

COPY ./service/nodejs/src /app

