#Move files into their respective folders

#Import required libraries
import os
import create
import directory
import menu
import write

#Initialize variables
root_path = os.getcwd() + '\\test'
files_txt = 'file_list.txt'
exts_txt = 'ext_list.txt'
sorting = True

while sorting:
  
  menu.main_menu()
  option = menu.select_opt()

  if option == 1:
    file_list = create.file_list(root_path)
  if option == 2:
    ext_list = create.ext_list(root_path)
  if option == 3:
    try:
      #Create directories for each extension type in ext_list
      directory.create_directory(root_path, ext_list)
    except:
      print('Could not create directories')
  if option == 4:
    # Write list of files to a txt file
    write.txt_list(file_list, files_txt)
  if option == 5:
    #Write list of found extensions to txt file
    write.txt_list(ext_list, exts_txt)
  if option == 6:
    directory.del_empty_dirs(root_path)
  if option == 7:
    sorting = False  

  print('---------------------------------------------------------------------------')

