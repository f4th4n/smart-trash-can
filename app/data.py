import numpy as np
import os
import sys
from skimage import io
from scipy.misc import imresize
from sklearn.model_selection import train_test_split
from skimage.color import gray2rgb
from app import config

# disable notice: Using TensorFlow backend.
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')
import keras
sys.stderr = stderr

# ----------------------------------------------------------------------------- private
dataset_path = 'data/train'

def get_imgs(labels):
  imgs = []
  for label in labels:
    data_path = dataset_path + '/' + label
    for file_name in os.listdir(data_path):
      img = get_img(data_path + '/' + file_name)
      imgs.append(img)
  return imgs

def create_x(imgs):
  X = np.zeros((len(imgs), config.img_size, config.img_size, 3), dtype='float64')
  for index, img in enumerate(imgs):
    if img.shape != (128, 128, 3):
      continue

    X[index] = img

  X /= 255.
  return X

def create_y(imgs, labels):
  Y = np.zeros(len(imgs))

  for label_key, label in enumerate(labels):
    data_path = dataset_path + '/' + label
    for counter, _ in enumerate(os.listdir(data_path)):
      Y[counter] = label_key

  Y = keras.utils.to_categorical(Y)
  return Y

# ----------------------------------------------------------------------------- public

def get_img(path):
  img = io.imread(path)
  img = imresize(img, (config.img_size, config.img_size, 3))
  # make sure every image is rgb
  if img.shape == (config.img_size, config.img_size):
    img = gray2rgb(img)
  return img

def get_data_set():
  labels = os.listdir(dataset_path)
  imgs = get_imgs(labels) # 
  X = create_x(imgs)
  Y = create_y(imgs, labels)

  X, X_test, Y, Y_test = train_test_split(X, Y, test_size=0.1, random_state=42)
  return X, X_test, Y, Y_test