# Import required libraries
import os
import write

def move_files(root_path, path_dictionary):
  """ Move all files found recursivley inside the root path. 
      root_path = root directory
      path_dictionary = dictionary of extensions and their corresponding directory (K = Ext: V = Path). """

  for dirpath, _, filenames in os.walk(root_path):
    for name in filenames:
      current_file_ext = name.split('.')[-1] # Current files extension.
      source = os.path.join(dirpath, name) # Source path of current file.
      destination = path_dictionary[current_file_ext] + '\\' + name # Path of where the file is to be moved. 
      try:
        shutil.move(source, destination)
      except:
        print('Destination does not exist')

def create_directory_dict(root_path, list_type):
  ''' Create a directory for all file names found.
      root_path = root passed in from menu instance.
      list_type = list of extensions or file names
        1. E.g. file_name.txt = txt 
        2. E.g. this file name [90932u4] = this file name  '''
  directory_dict = {}

  for item in list_type:
    try:
      new_dir_path = os.path.join(root_path, item)
      os.mkdir(new_dir_path)
      directory_dict[item] = new_dir_path
    except:
      if os.path.isdir(new_dir_path):
        print('Directory "{}" already exists'.format(item))
      else:
        print("Creation of the directory failed")
  
  return directory_dict

def del_empty_dirs(root_path):
  """ Delete all empty directories and subdirectories
      root_path = path of root folder passed in from menu instance. """
  choice = input('Are you sure you want to find and delete all empty directories? (Y/N): ').upper()
  deleted_dirs = [] # List to record deleted directories
  deleted_txt = 'deleted_dirs.txt' # Text file to view deleted directories

  while choice != 'Y' and choice != 'N':
    choice = input('That is not a valid selection, please press "Y" or "N": ').upper()
  
  if choice == 'Y':
    for dirpath, dirnames, files in os.walk(root_path):
      if len(dirnames) == 0 and len(files) == 0:
        try:
          os.rmdir(dirpath)
          deleted_dirs.append(dirpath)
        except:
          print('Directory is not empty')

    if len(deleted_dirs) > 0:
      print('All empty directories have been deleted')
      print('If you would like to review the directories deleted, please review the deleted_dirs.txt file')
      write.txt_list(deleted_dirs, deleted_txt)
    else:
      print('There were no empty directories to delete')

  else:
    print('Aborting')