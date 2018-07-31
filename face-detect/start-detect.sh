#!/bin/bash
#
# @Author: Bian
# @Abstract: run recognition-client on x86_64
# @Date: 2018.07.25

xhost +

docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix:0 -e GDK_SCALE -e GDK_DPI_SCALE --device /dev/video0:/dev/video0 -w / \
        face-detect\
        python /face-detec.py
