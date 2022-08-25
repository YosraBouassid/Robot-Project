import numpy as np
from PIL import Image
from tflite_runtime.interpreter import Interpreter
from flask import Flask
import requests
import time
import smbclient
import base64
from io import BytesIO

def set_input_tensor(interpreter, image):
  """Sets the input tensor."""
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = image

def get_output_tensor(interpreter, index):
  """Returns the output tensor at the given index."""
  output_details = interpreter.get_output_details()[index]
  tensor = np.squeeze(interpreter.get_tensor(output_details['index']))
  return tensor

def detect_objects(interpreter, image, threshold):
  """Returns a list of detection results, each a dictionary of object info."""
  set_input_tensor(interpreter, image)
  interpreter.invoke()

  # Get all output details
  boxes = get_output_tensor(interpreter, 0)
  classes = get_output_tensor(interpreter, 1)
  scores = get_output_tensor(interpreter, 2)
  count = int(get_output_tensor(interpreter, 3))

  results = []
  file2write=open("results.txt",'w')
  for i in range(count):
    if scores[i] >= threshold:
      result = {
          'bounding_box': boxes[i],
          'class_id': classes[i],
          'score': scores[i]
      }
      results.append(result)
      file2write.write(str(int(classes[i]))+',')
  file2write.close()
  return results

app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    interpreter = Interpreter('tmp/detect.tflite')
    interpreter.allocate_tensors()
    _, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']

    fd = smbclient.open_file(r"\\192.168.1.14\pi\public\image.txt", username="pi", password="pi", mode="r")
    data = fd.read()
    fd.close()
    image = Image.open(BytesIO(base64.b64decode(data))).convert('RGB')
    timestr = time.strftime("%Y%m%d-%H%M%S")
    image.save('history/capture_'+timestr+'.png','png')
    results = detect_objects(interpreter, image, 0.4)
    data = requests.get('http://192.168.1.14:5003/')
    print (data.text)
    return data.text

    
if __name__ == '__main__':
  app.run(host='192.168.1.13', port=5002)
