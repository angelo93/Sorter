# Import required libraries
import os
import shutil

def move_files(root_path, path_dictionary):
  """ Move all files found recursivley inside the root path. 
      root_path = root directory
      path_dictionary = dictionary of extensions and their corresponding directory (K = Ext: V = Path). """

  for dirpath, dirnames, filenames in os.walk(root_path):
    for name in filenames:
      current_file_ext = name.split('.')[-1] # Current files extension.
      source = os.path.join(dirpath, name) # Source path of current file.
      destination = path_dictionary[current_file_ext] + '\\' + name # Path of where the file is to be moved. 
      try:
        shutil.move(source, destination)
      except:
        print('Destination does not exist')