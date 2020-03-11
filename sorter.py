#Import required libraries
import os
import menu

#Initialize variables
sorting = True
new_menu = menu.MainMenu()
new_menu.show_menu()

while sorting:
  
  option = new_menu.get_opt()
  new_menu.create_file_and_ext_lists()
  
  if option == '6':
    sorting = False

  if option == 'M':
    new_menu.show_menu()

  new_menu.execute_opt(option)

