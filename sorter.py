#Move files into their respective folders

#Import required libraries
import os
import menu

#Initialize variables
root_path = os.getcwd() + '\\test'
files_txt = 'file_list.txt'
exts_txt = 'ext_list.txt'
sorting = True

while sorting:
  
  menu.main_menu()
  option = menu.select_opt()
  
  if option == 7:
    sorting = False

  menu.exe_opt(option, root_path, files_txt, exts_txt)

  print('---------------------------------------------------------------------------')

