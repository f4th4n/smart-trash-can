import sys
import os
from app import data
import numpy as np
from app import config

# disable notice: Using TensorFlow backend.
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')
import keras
sys.stderr = stderr

def get_model():
  # Getting model:
  model_file = open('data/model/model.json', 'r')
  model_json = model_file.read()
  model_file.close()
  model = keras.models.model_from_json(model_json)

  # Getting weights
  model.load_weights('data/model/weights.h5')
  return model

def predict(img_dir, model):
  img = data.get_img(img_dir)
  X = np.zeros((1, config.img_size, config.img_size, 3), dtype='float64')
  X[0] = img

  Y = model.predict(X, verbose=1)
  print(Y)
  keras.backend.clear_session()
  Y = np.argmax(Y, axis=1)
  max_val = Y[0]

  if max_val == 0:
    return 'this is organic'
  elif max_val == 1:
    return 'this is plastic'
  else:
    return 'this is unknown'
