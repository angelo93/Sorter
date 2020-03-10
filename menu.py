import create
import directory
import write
import config
import move

def main_menu():
  print('Press 1 to Create a list of files.')
  print('Press 2 to Create a list of extensions')
  print('Press 3 to Create a directory for all found extensions')
  print('Press 4 to Create a file listing all found files')
  print('Press 5 to Create a file listing all found extensions')
  print('Press 6 to delete all empty directories')
  print('Press 7 to files to corresponding directories')
  print('Press 8 to terminate program')

def select_opt():
  option = input('Please select an option: ')
  valid = ['1', '2', '3', '4', '5', '6', '7', '8']

  while option not in valid:
    option = input('That is not a valid option, please try again: ')
  
  return option

def exe_opt(option):
    if option == '1':
      config.file_list = create.file_list(config.root_path)
    if option == '2':
      config.ext_list = create.ext_list(config.root_path)
    if option == '3':
      try:
        #Create directories for each extension type in ext_list
        directory.create_directory(config.root_path, config.ext_list)
      except:
        print('Could not create directories')
    if option == '4':
      # Write list of files to a txt file
      write.txt_list(config.file_list, config.files_txt)
    if option == '5':
      # Write list of found extensions to txt file
      write.txt_list(config.ext_list, config.exts_txt)
    if option == '6':
      directory.del_empty_dirs(config.root_path)
    if option == '7':
      move.move_files()
    if option == '8':
      print('Terminating program')