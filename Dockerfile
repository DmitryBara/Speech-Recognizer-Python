FROM python:3.8.3-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN apk update \
    && apk add --update py-pip \
    && apk add build-base


COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .