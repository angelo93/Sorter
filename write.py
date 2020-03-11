# Import required libraries
import os

# Path of folder to hold text files created.
save_path = os.getcwd() + '\\lists'

def make_dir():
  """ Make the folder hold text files. """

  try:
    os.mkdir(save_path)
  except:
    print('Folder for lists already exists, proceeding to write file')

def txt_list(list_name, file_name):
  """ Record elements in a given list to a text file for reference. """

  # Create the complete path name for the text file.
  complete_name = os.path.join(save_path, file_name)

  # Call make_dir to make the text folder in case it's not present.
  make_dir()

  with open(complete_name, "w") as text_file:
    for item in list_name:
      text_file.write(item + '\n')

  text_file.close()
