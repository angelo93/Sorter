#Import required libraries
import os
import menu
import config

#Initialize variables
sorting = True

while sorting:
  
  menu.main_menu()
  option = menu.select_opt()
  
  if option == '8':
    sorting = False

  menu.exe_opt(option)

  print('---------------------------------------------------------------------------')

