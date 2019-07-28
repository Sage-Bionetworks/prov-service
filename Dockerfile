FROM python:3.6-alpine

RUN apk update && \
    apk upgrade && \
    apk add --no-cache bash curl

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080
