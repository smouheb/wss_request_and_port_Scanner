FROM python:3.10.4-slim-buster

RUN apt update && \
    apt install nmap -y && \
    mkdir app

COPY ./ app

WORKDIR /app

RUN pip install -r requirements.txt
