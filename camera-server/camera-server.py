# Camera Server
# 
# @Author: Bian
# @Abstract: Camera Server runs in a container at port 5000 of the host, 
# takes pictures and sends them to the port.
# @Date: 2018.06.14

from importlib import import_module
import os
from flask import Flask, render_template, Response

# comment this out if you're not using USB webcam
from camera_opencv import Camera

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world!"

def gen2(camera):
    """Returns a single image frame"""
    frame = camera.get_frame()
    yield frame

@app.route('/image.jpg')
def image():
    """Returns a single current image for the webcam"""
    return Response(gen2(Camera()), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
