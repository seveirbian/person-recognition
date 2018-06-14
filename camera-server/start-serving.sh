#!/bin/bash
#
# @Author: Bian
# @Abstract: run camera-server in a container
# @Date: 2018.06.14

docker run -d --name server --rm \
        -p 127.0.0.1:5000:5000 \
        --device /dev/video0:/dev/video0 \
        seveirroy/camera-server
