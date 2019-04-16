import sys
import os
import shutil
from app import summary

def setup():
  logs_path = 'data/logs'
  if os.path.exists(logs_path):
    shutil.rmtree(logs_path)
  os.makedirs(logs_path)

def start_by_mode(mode):
  if mode == '1' or mode == 'train':
    from app import train
    train.train()
  elif mode == '2' or mode == 'predict':
    from app import predict
    if len(sys.argv) == 3:
      img_path = sys.argv[2]
    else:
      img_path = input('Enter image path: ')

    model = predict.get_model()
    prediction = predict.predict(img_path, model)
    print(prediction)
  elif mode == '3' or mode == 'start_server':
    from app import server
    app = server.get_app()
    app.run(debug=True, host='0.0.0.0', port=19000)
  elif mode == '4' or mode == 'generate_oidv4':
    if len(sys.argv) == 3:
      label = sys.argv[2]
    else:
      label = input('Enter oidv4 label: ')

    from app import generate_oidv4
    generate_oidv4.generate(label)
  elif mode == '5' or mode == 'augment_data':
    from app import augmentor
    if len(sys.argv) == 3:
      img_dir = sys.argv[2]
    else:
      img_dir = input('Enter image directory: ')
    augmentor.start(img_dir)
  elif mode == 'q':
    exit()

def app():
  if len(sys.argv) > 1:
    mode = sys.argv[1]
    start_by_mode(mode)
    exit()

  summary.summary()

  print("""
Command:
1: train
2: predict
3: start server
4: prepare data: generate oidv4
5: prepare data: augment data
q: quit
  """)

  while True:
    mode = input('Enter command:')
    start_by_mode(mode)

setup()
app()