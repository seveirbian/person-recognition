FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends python python-opencv
    
ADD face-detection.tar.gz /

CMD python /face-detection/face-detec.py
