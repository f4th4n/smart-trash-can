import os
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from keras.callbacks import ModelCheckpoint, TensorBoard
from app import config

def save_model(model):
  model_json = model.to_json()
  with open('data/model/model.json', 'w') as model_file:
    model_file.write(model_json)
  # serialize weights to HDF5
  model.save_weights('data/model/weights.h5')
  print('Model and weights saved')
  return

def get_model(num_classes=2):
  model = Sequential()

  model.add(Conv2D(32, (3, 3), input_shape=(config.input_shape, config.input_shape, 3)))
  model.add(Activation('relu'))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Conv2D(32, (3, 3)))
  model.add(Activation('relu'))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Conv2D(config.input_shape, (3, 3)))
  model.add(Activation('relu'))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Flatten())
  model.add(Dense(config.input_shape))
  model.add(Activation('relu'))
  model.add(Dropout(0.5))
  model.add(Dense(num_classes))
  model.add(Activation('softmax'))

  model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=['accuracy'])

  return model

def get_checkpoints():
  checkpoints = []
  checkpoints.append(ModelCheckpoint('data/model/best_weights.h5', monitor='val_loss', verbose=0, save_best_only=True, save_weights_only=True, mode='auto', period=1))
  checkpoints.append(TensorBoard(log_dir='data/logs', histogram_freq=0, write_graph=True, write_images=False, embeddings_freq=0, embeddings_layer_names=None, embeddings_metadata=None))
  return checkpoints
