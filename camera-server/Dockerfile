FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y python python-pip python-opencv wget && \
    pip install flask && \
    wget && \
    apt-get rm python-pip wget -y


WORKDIR /camera-server/
CMD python camera-server.py
