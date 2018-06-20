#!/bin/bash
#
# @Author: Bian
# @Abstract: run recognition-client on x86_64
# @Date: 2018.06.20

xhost +

docker run -d --name recognition-client --rm \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -e DISPLAY=unix$DISPLAY \
        -e GDK_SCALE \
        -e GDK_DPI_SCALE \
        -w /recongnition-client \
        seveirroy/recognition-client \
        python3 recognition-client.py 10.11.33.62:5000