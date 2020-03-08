import os
import config

save_path = os.getcwd() + '\\lists'

def make_dir():
  try:
    os.mkdir(save_path)
  except:
    print('List folder already exists proceeding to write file')

def txt_list(list_name, file_name):
  complete_name = os.path.join(save_path, file_name)

  make_dir()

  with open(complete_name, "w") as text_file:
    for item in list_name:
      text_file.write(item + '\n')

  text_file.close()
