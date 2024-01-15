FROM python:3.12.1-bullseye

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt