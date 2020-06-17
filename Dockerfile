# First line is the image that you gona inherit dockerfile from 
# Image used 3.8 alpine

FROM python:3.8-alpine
# Next line is optional, reffered to maintener
# MAINTAINER miyato development Ltd maintainer je depracated in the meantime

# This env is recomended
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# -D create user who will only run applications, recomended to avoid compromising usage of app
RUN adduser -D user
USER user

# After setup command for build is:
# $ docker build .
# error fixed on : https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue