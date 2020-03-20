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

def create_alpha_dirs(root_path):
  ''' Creates alphabetical directories to organize subdirectories. 
      /A --> /A/A_dir
         --> /A/Another_dir. '''

  alpha_dirs = [
    root_path + '/' + '#',
    root_path + '/' + 'Other'
  ]

  for letter in string.ascii_uppercase:
    alpha_dirs.append(root_path + '/' + letter)

  for dirname in alpha_dirs:
    try:
      os.mkdir(dirname)
    except FileExistsError:
      print('The directory "{}" already exists.'.format(dirname))

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

def org_by_alpha(root_path):
  ''' Organize subdirectories alphabetically. '''

  create_alpha_dirs(root_path)

  for dirpath, dirnames, _ in os.walk(root_path):
    dirnames[:] = [
      d for d in dirnames if not d.startswith('.') and 
      d[0] not in string.ascii_uppercase and 
      d[0] != '#' and 
      d[0] != 'Other'
    ]
    for dirname in dirnames:
      source = os.path.join(dirpath, dirname).replace('\\', '/')
      if dirname[0].isalpha():
        destination = os.path.join(dirpath.replace('\\', '/'), dirname[0].upper(), dirname)
      elif dirname[0].isdigit():
        destination = os.path.join(dirpath.replace('\\', '/'), '#', dirname)
      else:
        destination = os.path.join(dirpath.replace('\\', '/'), 'Other', dirname)
      try:
        if os.path.isdir(destination):
          shutil.copytree(source, destination, dirs_exist_ok=True)
          shutil.rmtree(source)
        else:
          shutil.move(source, destination)
      except FileNotFoundError:
        print('The destination directory does not exist.')
 
def move_files(root_path, split_char = '.', index = -1):
  """ Move all files found recursivley inside the root path. 
      root_path = root directory. """

  for dirpath, _, filenames in os.walk(root_path):
    # Skip hidden files.
    filenames = [f for f in filenames if not f[0] == '.']
    for name in filenames:
      current_file = name.split(split_char)[index].strip() # If split_char == '.', file's extension otherwise file's name
      source = os.path.join(dirpath, name) # Source path of current file.
      destination = os.path.join(root_path, current_file, name)
      try:
        shutil.move(source, destination)
      except FileExistsError:
        print('The file "{}" already exists.'.format(destination))
      except FileNotFoundError:
        print('Source "{}" does not exist'.format(source))

def write_txt_list(list_name, file_name):
  """ Record elements in a given list to a text file for reference. """
  
  save_path = os.getcwd() + '\\logs'

  def make_logs_dir(file_name):
    """ Make the folder to hold text files. """
    
    try:
      os.mkdir(save_path)
    except FileExistsError:
      print('Folder for lists already exists, proceeding to write {}'.format(file_name))

  # Create the complete path name for the text file.
  complete_name = os.path.join(save_path, file_name)

  # Call make_dir to make the text folder in case it's not present.
  make_logs_dir(file_name)

  with open(complete_name, "w", encoding='utf-8') as text_file:
    for item in list_name:
      text_file.write(item + '\n')

  text_file.close()
