import create
import directory
import write
import config
import move

def main_menu():
  print('To Create a list of files, press 1.')
  print('To Create a list of extensions, press 2.')
  print('To Create a directory for all found extensions, press 3.')
  print('To Create a file listing all found files, press 4.')
  print('To Create a file listing all found extensions, press 5.')
  print('To delete all empty directories, press 6.')
  print('If you would like to quit, press 7.')

def select_opt():
  option = int(input('Please select an option: '))
  valid = [1, 2, 3, 4, 5, 6, 7, 8]

  while option not in valid:
    option = int(input('That is not a valid option, please try again: '))
  
  return option

def exe_opt(option, root_path):
    if option == 1:
      config.file_list = create.file_list(root_path)
    if option == 2:
      config.ext_list = create.ext_list(root_path)
    if option == 3:
      try:
        #Create directories for each extension type in ext_list
        directory.create_directory(root_path, config.ext_list)
      except:
        print('Could not create directories')
    if option == 4:
      # Write list of files to a txt file
      write.txt_list(config.file_list, config.files_txt)
    if option == 5:
      # Write list of found extensions to txt file
      write.txt_list(config.ext_list, config.exts_txt)
    if option == 6:
      directory.del_empty_dirs(root_path)
    if option == 7:
      print('Terminating program')
    if option == 8:
      move.move_files()