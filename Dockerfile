FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y
RUN apt-get install apt-utils python3.8-dev python3-pip git -y
RUN apt-get install portaudio19-dev alsa-base alsa-utils -y

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install --upgrade setuptools
RUN pip install -r requirements.txt