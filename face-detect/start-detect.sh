#!/bin/bash
#
# @Author: Bian
# @Abstract: run recognition-client on x86_64
# @Date: 2018.07.25

xhost +

docker run -it --rm --name face-detect \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -e DISPLAY=unix$DISPLAY \
        -e GDK_SCALE \
        -e GDK_DPI_SCALE \
        -w / \
        face-detect \
        /bin/bash
