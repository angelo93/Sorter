#Move files into their respective folders

#Import required libraries
import os
import menu
import config

#Initialize variables
sorting = True

while sorting:
  
  menu.main_menu()
  option = menu.select_opt()
  
  if option == 7:
    sorting = False

  menu.exe_opt(option, config.root_path, config.files_txt, config.exts_txt)

  print('---------------------------------------------------------------------------')

