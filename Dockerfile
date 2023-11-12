FROM python:3.11-slim-buster

LABEL org.opencontainers.image.authors="Cristian Ordoñez"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

RUN prisma generate
