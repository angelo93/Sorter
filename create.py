import os
import config

def file_list(root_path):
  file_list = []

  #Create a list of files in the root directory
  for dirpath, dirnames, files in os.walk(root_path):
      for file in files:
        file_list.append(file)

  return file_list

def ext_list(root_path):
  ext_list = []

  #Create a list of all found extensions
  for dirpath, dirnames, files in os.walk(root_path):
      for file in files:
        ext_list.append(file.split('.')[-1])

  return ext_list
