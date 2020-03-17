#Import required libraries
import os
import menu

#Initialize variables
sorting = True
new_menu = menu.MainMenu()
new_menu.show_menu()
new_menu.create_lists()

while sorting:
  
  option = new_menu.get_opt()
  new_menu.execute_opt(option)

