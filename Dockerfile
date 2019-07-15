FROM python:3-alpine

RUN apk update && \
    apk upgrade && \
    apk add --no-cache bash

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
RUN chmod a+x /usr/src/app/wait-for-it.sh
RUN export 'PATH=$PATH:${PWD}'

EXPOSE 8080
