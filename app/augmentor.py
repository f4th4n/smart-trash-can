import Augmentor

def start(img_dir):
  print('-------------------------')
  print('-------------------------')
  print('-------------------------')
  print('result on: ' + img_dir + '/output')
  print('-------------------------')
  print('-------------------------')
  print('-------------------------')
  p = Augmentor.Pipeline(img_dir)
  p.rotate90(probability=0.5)
  p.rotate270(probability=0.5)
  p.flip_left_right(probability=0.8)
  p.flip_top_bottom(probability=0.3)
  p.skew(probability=0.5)
  p.random_distortion(probability=0.8, grid_width=4, grid_height=4, magnitude=8)
  p.sample(500)
  print('finished\n')
