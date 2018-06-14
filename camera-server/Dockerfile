FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y python python-pip python-opencv wget git && \
    pip install flask

WORKDIR /

RUN mkdir camera-server

WORKDIR /camera-server/

RUN wget https://raw.githubusercontent.com/seveirbian/face-recognition/master/camera-server/base_camera.py && \
    wget https://raw.githubusercontent.com/seveirbian/face-recognition/master/camera-server/camera-server.py && \
    wget https://raw.githubusercontent.com/seveirbian/face-recognition/master/camera-server/camera_opencv.py
 
RUN apt-get remove python-pip wget git -y

CMD python camera-server.py
