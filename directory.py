import os
import write

def create_directory(root_path, ext_list):
  for ext in ext_list:
    try:
      new_dir_path = os.path.join(root_path, ext)
      os.mkdir(new_dir_path)
    except:
      if os.path.isdir(new_dir_path):
        print('Directory "{}" already exists'.format(ext))
      else:
        print("Creation of the directory failed")

def del_empty_dirs(root_path):
  choice = input('Are you sure you want to find and delete all empty directories? (Y/N): ').upper()
  deleted_dirs = []
  deleted_txt = 'deleted_dirs.txt'

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