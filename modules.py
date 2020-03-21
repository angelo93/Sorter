''' This file stores all helper functions. '''

# Import required libraries
import os
import shutil
import string

def create_directory(root_path, list_type):
  ''' Create a directory for all files either by file name or extension and returns a dictionary.
      root_path = root passed in from menu instance.
      list_type = list of extensions or file names
        1. E.g. file_name.txt = txt 
        2. E.g. this file name [90932u4] = this file name (split on "["). '''

  for item in list_type:
    new_dir_path = os.path.join(root_path, item)
    try:
      os.mkdir(new_dir_path)
      print('Directory "{}" created.'.format(item))
    except:
      if os.path.isdir(new_dir_path):
        print('Directory "{}" already exists.'.format(item))
      else:
        print("Creation of {} directory failed.".format(item))

def del_empty_dirs(root_path):
  """ Delete all empty directories and subdirectories
      root_path = path of root folder passed in from menu instance. """
      
  choice = input('Are you sure you want to find and delete all empty directories? (Y/N): ').upper()
  deleted_dirs = [] # List to record deleted directories
  deleted_txt = 'deleted_dirs.txt' # Text file to view deleted directories

  while choice != 'Y' and choice != 'N':
    choice = input('That is not a valid selection, please press "Y" or "N": ').upper()
  
  if choice == 'Y':
    for dirpath, dirnames, _ in os.walk(root_path, topdown=False):
      dirnames[:] = [d for d in dirnames if not d.startswith('.')]
      try:
        os.rmdir(dirpath)
        deleted_dirs.append(dirpath)
      except:
        print('{} is not empty'.format(dirpath))

    if len(deleted_dirs) > 0:
      print('All empty directories have been deleted')
      print('If you would like to review the directories deleted, please review the deleted_dirs.txt file')
      write_txt_list(deleted_dirs, deleted_txt)
    else:
      print('There were no empty directories to delete')
  else:
    print('Empty directories will not be deleted.')

def move_files(root_path, split_char = '.', index = -1, organize = False, by_ext = True):
  parent = ''
  
  dirs_to_skip = [char for char in string.ascii_uppercase] 
  dirs_to_skip.append('#')
  dirs_to_skip.append('Other')

  for dirpath, _, filenames in os.walk(root_path):
    # Skip hidden directories.
    if dirpath.split('\\')[-1].startswith('.') or dirpath.split('\\')[-1] in dirs_to_skip:
      continue
    for name in filenames:
      # Skip hidden files.  
      if name.startswith('.'):
        continue
      if organize and not by_ext:
        if name[0].isdigit():
          parent = '#'
        elif name[0].isalpha():
          parent = name[0].upper()
        else:
          parent = 'Other'
      elif organize and by_ext:
        if name.split(split_char)[index][0].isdigit():
          parent = '#'
          print(parent)
        elif name.split(split_char)[index][0].isalpha():
          parent = name.split(split_char)[index][0].upper()
          print(parent)
        else:
          parent = 'Other'
      current_file = name.split(split_char)[index].strip() # If split_char == '.', file's extension otherwise file's name
      source = os.path.join(dirpath, name).replace('\\', '/') # Source path of current file.
      destination = os.path.join(root_path, parent, current_file, name).replace('\\', '/')
      try:
        os.makedirs(os.path.join(root_path, parent, current_file), exist_ok=True)
        shutil.move(source, destination)
      except FileExistsError:
        print('The file "{}" already exists.'.format(destination))
      except FileNotFoundError:
        print('Source "{}" does not exist'.format(source))

def write_txt_list(list_name, file_name):
  """ Record elements in a given list to a text file for reference. """
  def make_logs_dir(file_name):
    """ Make the folder to hold text files. """
    try:
      os.mkdir(save_path)
    except FileExistsError:
      print('Folder for lists already exists, proceeding to write {}'.format(file_name))
  
  save_path = os.getcwd() + '\\logs'

  # Create the complete path name for the text file.
  complete_name = os.path.join(save_path, file_name)

  # Call make_dir to make the text folder in case it's not present.
  make_logs_dir(file_name)

  with open(complete_name, "w", encoding='utf-8') as text_file:
    for item in list_name:
      text_file.write(item + '\n')

  text_file.close()
