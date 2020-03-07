#Move files into their respective folders

#Import required libraries
import os

#Initialize variables
root_path = "C:/Users/Angel/Desktop/Projects/Main/Sorter/test"
files_txt = 'file_list.txt'
exts_txt = 'ext_list.txt'
sorting = True

def createFileList(root_path):
  file_list = []

  #Create a list of files in the root directory
  for dirpath, dirnames, files in os.walk(root_path):
      for file in files:
        file_list.append(file)

  return file_list

def createExtList(root_path):
  ext_list = []

  #Create a list of all found extensions
  for dirpath, dirnames, files in os.walk(root_path):
      for file in files:
        ext_list.append(file.split('.')[-1])

  return ext_list

def writeList(list_name, file_name):
  with open(file_name, "w") as text_file:
    for item in list_name:
      text_file.write(item + '\n')

  text_file.close()

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

def delEmptyDirs(root_path):
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
      writeList(deleted_dirs, deleted_txt)
    else:
      print('There were no empty directories to delete')
  else:
    print('Aborting')

def sortingMenu():
  print('To Create a list of files, press 1.')
  print('To Create a list of extensions, press 2.')
  print('To Create a directory for all found extensions, press 3.')
  print('To Create a file listing all found files, press 4.')
  print('To Create a file listing all found extensions, press 5.')
  print('To delete all empty directories, press 6.')
  print('If you would like to quit, press 7.')

def selectOption():
  option = int(input('Please select an option: '))
  valid = [1, 2, 3, 4, 5, 6, 7]

  while option not in valid:
    option = int(input('That is not a valid option, please try again: '))
  
  return option

while sorting:
  
  sortingMenu()
  option = selectOption()

  if option == 1:
    file_list = createFileList(root_path)
  if option == 2:
    ext_list = createExtList(root_path)
  if option == 3:
    try:
      #Create directories for each extension type in ext_list
      create_directory(root_path, ext_list)
    except:
      print('Could not create directories')
  if option == 4:
    # Write list of files to a txt file
    writeList(file_list, files_txt)
  if option == 5:
    #Write list of found extensions to txt file
    writeList(ext_list, exts_txt)
  if option == 6:
    delEmptyDirs(root_path)
  if option == 7:
    sorting = False  

  print('---------------------------------------------------------------------------')

