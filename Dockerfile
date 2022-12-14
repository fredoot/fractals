# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY . .

RUN chmod +x docker-entrypoint.sh

