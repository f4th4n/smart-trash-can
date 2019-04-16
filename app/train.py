from app import data
from app import model as Model

def train():
  X, X_test, Y, Y_test = data.get_data_set()
  model = Model.get_model()
  model.fit(X, Y, batch_size=10, epochs=40, validation_data=(X_test, Y_test), shuffle=True, callbacks=Model.get_checkpoints())
  Model.save_model(model)
  print('finished training')