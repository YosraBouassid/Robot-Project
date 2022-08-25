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
import os
import base64
from datetime import datetime

app = Flask(__name__)

def date_diff_in_Seconds(dt2, dt1):
  timedelta = float((dt2.microsecond+(dt2.second*1000000))-(dt1.microsecond+(dt1.second*1000000)))
  return (timedelta/1000000)/60

@app.route("/", methods=['GET'])
def main():
  interpreter = Interpreter('tmp/detect.tflite')
  interpreter.allocate_tensors()
  _, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']

  with picamera.PiCamera(resolution=(320, 240), framerate=30) as camera:
    try:
      stream = io.BytesIO()
      file2write1= open("latence.txt",'w')
      file2write1.write("")
      file2write1.close()
      for _ in camera.capture_continuous(stream, format='jpeg', use_video_port=True):
        stream.seek(0)        
        image = Image.open(stream).convert('RGB').resize((input_width, input_height), Image.ANTIALIAS)
        image.save('capture.png', 'png')
        with open("capture.png", "rb") as image_file:
            data = base64.b64encode(image_file.read())
            file2write=open("image.txt",'w')
            file2write.write(str(data,'utf-8'))
            file2write.close()
        date1 = datetime.now()   
        data = requests.get('http://192.168.1.13:5002/')
        date2 = datetime.now()
        val = data.text
        print (val)
        stream.seek(0)
        stream.truncate()
        
        print("\n%f" %(date_diff_in_Seconds(date2, date1)))
        file2write1= open("latence.txt",'a')
        file2write1.write(str(date_diff_in_Seconds(date2, date1))+"\n")
        file2write1.close()
        

    finally:
      camera.stop_preview()

if __name__ == '__main__':
    app.run(host='192.168.1.14', port=5001)