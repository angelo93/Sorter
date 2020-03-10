import os
import shutil
import config

def move_files():
  for dirpath, dirnames, files in os.walk(config.root_path):
    for file in files:
      current_file_ext = file.split('.')[-1]
      source = os.path.join(dirpath, file)
      destination = config.directory_ext_dict[current_file_ext] + '\\' + file
      try:
        shutil.move(source, destination)
      except:
        print('Destination does not exist')