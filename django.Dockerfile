FROM python:3.10-slim

RUN apt-get update && apt-get upgrade -y && apt-get install git -y

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /backend
RUN mkdir static

COPY ./django/requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./django/ /backend

