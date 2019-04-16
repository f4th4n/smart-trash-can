from app import predict
from flask import Flask, request
import base64
import time
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome_get():
  str = """
    <style>
      input {
        font-size: 150%;
      }
    </style>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <input id="file" type="file" accept="image/*" onchange="test()">
    <form method="post" action="/" enctype='multipart/form-data'>
      <input id="base64img" name="img" type="text" />
      <br />
      <input type="submit" value="Submit" />
    </form>

    <script>
      function setBase64(file) {
         var reader = new FileReader();
         reader.readAsDataURL(file);
         reader.onload = function () {
           console.log(reader.result);
           document.getElementById('base64img').value = reader.result
         };
         reader.onerror = function (error) {
           console.log('Error: ', error);
         };
      }

    function test() {
      const $file = document.getElementById('file')
      setBase64($file.files[0])
    }
    </script>
  """
  return str
 
@app.route('/', methods=['POST'])
def welcome_post():
  model = predict.get_model()
  img_str = request.form.get('img')
  img_str_clean = img_str.replace('data:image/jpeg;base64,', '').replace('data:image/png;base64,', '')

  img_data = base64.b64decode(img_str_clean)
  ts = time.time()
  file_name = '/tmp/' + str(ts) + '.jpg'
  with open(file_name, 'wb') as f:
    f.write(img_data)

  prediction = predict.predict(file_name, model)

  #  if prediction == 'adalah organic':
  #    os.system('xdotool key 1 && xdotool key 0')
  #  else:
  #    os.system('xdotool key 2 && xdotool key 0')

  return '<h1>Prediction:  ' + prediction + '</h1><br /><br /><a href="/">Home</a>'

def get_app():
  return app
