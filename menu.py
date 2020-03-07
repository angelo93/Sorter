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
  valid = [1, 2, 3, 4, 5, 6, 7]

  while option not in valid:
    option = int(input('That is not a valid option, please try again: '))
  
  return option