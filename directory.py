# Import required libraries
import os
import write

def create_directory(root_path, ext_list):
  """ Create directory for all found file extensions
      root_path = path passed in from menu instance
      ext_list = list of found extensions in root path. """
  directory_ext_dict = {} # create a dictionary of extensions and corresponding directories

  # For every extension create a directory
  for ext in ext_list:
    try: 
      new_dir_path = os.path.join(root_path, ext)
      os.mkdir(new_dir_path)
      directory_ext_dict[ext] = new_dir_path # Add new dir path to the dict as the value of the extension
    except:
      if os.path.isdir(new_dir_path):
        print('Directory "{}" already exists'.format(ext))
      else:
        print("Creation of the directory failed")
  
  return directory_ext_dict

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