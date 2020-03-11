import os
import shutil

def move_files(root_path, path_dictionary):
  for dirpath, dirnames, files in os.walk(root_path):
    for file in files:
      current_file_ext = file.split('.')[-1]
      source = os.path.join(dirpath, file)
      destination = path_dictionary[current_file_ext] + '\\' + file
      try:
        shutil.move(source, destination)
      except:
        print('Destination does not exist')