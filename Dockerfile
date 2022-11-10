# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY . .

#RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["/bin/sh", "./docker-entrypoint.sh"]

