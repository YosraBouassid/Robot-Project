#perception-->navigation-->decision
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import io
import re
import time
import numpy as np
import picamera
from PIL import Image
from tflite_runtime.interpreter import Interpreter
from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar
import cv2
import numpy as np
from flask import Flask
import requests
import smbclient

app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    bw = back_wheels.Back_Wheels()
    picar.setup()
    bw.speed = 0
    with smbclient.open_file(r"\\192.168.1.13\pi\public\results.txt", username="pi", password="pi", mode="r") as fd:
        data = fd.read()
        existList = data.split(',')
        print (existList)
        if ('0' in existList):
            bw.speed = 0
            return '0'
        else:
            bw.speed = 60
            return '60'
if __name__ == '__main__':
    app.run(host='192.168.1.14', port=5003)