import os
from PIL import Image
import shutil

# ----------------------------------------------------------------------------- private

def create_and_cut_img(file_name, left, top, right, bot):
  pil_img = Image.open(file_name)
  pil_img = pil_img.crop((left, top, right, bot))
  return pil_img

def save_img(pil_img, file_name):
  pil_img.save(data_oidv4_path + '/' + file_name)

def generate_img(label_content, label_path, class_name, train_path):
  #left, top, right, bot
  label_content = label_content.replace(class_name + ' ', '')
  lines = label_content.split('\n')
  for line in lines:
    chunks = line.split(' ')
    if len(chunks) < 4:
      continue

    left = float(chunks[0])
    top = float(chunks[1])
    right = float(chunks[2])
    bot = float(chunks[3])
    img_path = train_path + '/' + label_path.replace('txt', 'jpg')
    pil_img = create_and_cut_img(img_path, left, top, right, bot)
    img_file_name = os.path.basename(img_path)
    save_img(pil_img, img_file_name)

def prepare(data_oidv4_path):
  if os.path.exists(data_oidv4_path):
    shutil.rmtree(data_oidv4_path)

  os.makedirs(data_oidv4_path)

# ----------------------------------------------------------------------------- public

def generate(class_name):
  train_path = 'app/OIDv4_ToolKit/OID/Dataset/train/' + class_name
  train_labels_path = train_path + '/Label'
  data_oidv4_path = 'data/oidv4/' + class_name
  prepare(data_oidv4_path)

  labels_file_name = os.listdir(train_labels_path)
  for index, file_name in enumerate(labels_file_name):
    fd = open(train_labels_path + '/' + file_name, 'r')
    for label_content in fd:
      generate_img(label_content, file_name, class_name, train_path)

  print('finished. See ' + data_oidv4_path)