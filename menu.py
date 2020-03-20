# Import required libraries
import modules
import os
import sys

class MainMenu():
  ''' Class dealing with the display of menus and realization of options. 

    self.root, The root path directory to be sorted, default is directory where script is located.
    self.files_txt, Filename for creating a text file of all found files.
    self.exts_txt, Filename for creating a text file of all found extensions.
    self.file_name_txt, Filename for creating a text file of all found file names.
    self.ext_list, List to hold all extensions.
    self.file_list, List to hold all found files.
    self.file_name_list, List to hold all found file names.
    self.passes, Simple variable to check how many times the user has selected an option.
    self.split_char, Variable to specify which character to split file names on. '''

  def __init__(self, root_path = os.getcwd()):
    self.root = root_path + '\\test' # The root path directory to be sorted, default is directory where script is located.
    self.files_txt = 'file_list.txt' # Filename for creating a text file of all found files.
    self.exts_txt = 'ext_list.txt' # Filename for creating a text file of all found extensions.
    self.file_name_txt = 'file_name_list.txt' # Filename for creating a text file of all found file names.
    self.ext_list = [] # List to hold all extensions.
    self.file_list = [] # List to hold all found files.
    self.file_name_list = [] # List to hold all found file names.
    self.passes = 0 # Simple variable to check how many times the user has selected an option.
    self.split_char = '' # Variable to specify which character to split file names on.

  def clear_screen(self):
    os.system('cls' if os.name=='nt' else 'clear')

  def show_menu(self):
    ''' Show main options to user. '''

    print('Press 1 to create directories.')
    print('Press 2 to create logs.')
    print('Press 3 to delete all empty directories.')
    print('Press 4 to move files to corresponding directories.')
    print('Press 5 to change root directory.')
    print('press 6 to re-generate file and extensions lists.')
    print('Press 7 to terminate program.')
    print('-' * 100)

  def get_opt(self):
    ''' Get option from user. '''

    # Check to see if first time called.
    if self.passes == 0:
      option = input('Please select an option: ').upper()
    else:
      print('If you would like to look at the main menu, press "M".')
      option = input('Please select another option: ').upper()
      print('-' * 100)

    # List of valid inputs
    valid = ['1', '2', '3', '4', '5', '6', '7', 'M']

    # If option is not a valid option, ask user again.
    while option not in valid:
      print('If you would like to look at the main menu, press "M".')
      option = input('That is not a valid option, please try again: ')
      print('-' * 100)
    
    self.passes += 1
    return option

  def execute_opt(self, option):
    ''' Execute the chosen option of the user. 
        option = option passed in from user. '''

    if option == '1':
      self.clear_screen()
      # Create directories of a particular type
      self.option_one()
    if option == '2':
      self.clear_screen()
      # Write files using generated lists
      self.option_two()
    if option == '3':
      self.clear_screen()
      # Delete all empty directories and subdirectories.
      modules.del_empty_dirs(self.root)
      print('-' * 100)
    if option == '4':
      self.clear_screen()
      # Move found files to directory corresponding to their extension.
      self.option_four()
    if option == '5':
      self.clear_screen()
      self.option_five()
    if option == '6':
      self.clear_screen()
      self.create_lists()
    if option == '7':
      self.clear_screen()
      print('Terminating program')
      sys.exit()
    if option == 'M':
      self.clear_screen()
      self.show_menu()

  def option_one(self):
    ''' Function to decide what kind of directories to create. '''

    print('Press 1 to create directories for found extensions')
    print('Press 2 to create directories for found file names')
    
    choice = input('Please select an option: ')
    valid = ['1', '2']

    while choice not in valid:
      choice = input('That is not a valid option, please try again: ')
    if choice == '1':
      try:
        #Create directories for each extension type in ext_list.
        modules.create_directory(self.root, self.ext_list)
      except:
        print('Could not create directories')
    if choice == '2':
      try:
        #Create directories for each file name in file_name_list.
        modules.create_directory(self.root, self.file_name_list)
      except:
        print('Could not create directories')
    print('-' * 100)

  def option_two(self):
    ''' Create a file listing either all
          extensions, files and or file names. '''

    print('Press 1 to create a file listing all extensions.')
    print('Press 2 to create a file listing all files.')
    print('Press 3 to create a file listing all file names.')
    print('Press 4 to create all files.')
    
    choice = input('Please select an option: ')
    valid = ['1', '2', '3', '4']

    while choice not in valid:
      choice = input('That is not a valid option, please try again: ')
    if choice == '1':
      # Write list of files to a txt file.
      modules.write_txt_list(self.file_list, self.files_txt)
    if choice == '2':
      # Write list of found extensions to txt file.
      modules.write_txt_list(self.ext_list, self.exts_txt)
    if choice == '3':
      # Write list of found extensions to txt file.
      modules.write_txt_list(self.file_name_list, self.file_name_txt)
    if choice == '4':
      # Write all files from above options
      modules.write_txt_list(self.file_list, self.files_txt)
      modules.write_txt_list(self.ext_list, self.exts_txt)
      modules.write_txt_list(self.file_name_list, self.file_name_txt)
    print('-' * 100)

  def option_four(self):
    ''' Decide whether user is moving files based on their extensions or names
        and would also like to organize directories into alphabetical folders. '''

    print('Press 1 to move files based on their extensions')
    print('Press 2 to move files based on their names')

    choice = input('Please select an option: ')
    valid = ['1', '2']

    while choice not in valid:
      choice = input('That is not a valid option, please try again: ')
    if choice == '1':
      modules.move_files(self.root)
    if choice == '2':
      modules.move_files(self.root, self.split_char, 0)

    org_dirs = input('Would you like to organize the directories into alphabetical folders? (Y/N): ').upper()

    while org_dirs != 'Y' and org_dirs != 'N':
      org_dirs = input('Please press "Y" or "N" to organize directories into alphabetical folders: ').upper()

    if org_dirs == 'Y':
      print('It is recommended that you delete all current empty directories to avoid errors.')
      modules.del_empty_dirs(self.root)
      modules.org_by_alpha(self.root)
    print('-' * 100)
  
  def option_five(self):
    ''' Change root directory path and reset file, extension and file name lists.'''

    # Get new path from user.
    new_dir_path = input('Please provide the new root directory path:\n')

    # Check to see if new path exists, 
    if os.path.isdir(new_dir_path): # If yes, change current to root to new root and create new lists.
      self.root = new_dir_path.replace('\\', '/')
      self.create_lists()
    else:
      print('That directory {} does not exist.'.format(new_dir_path))

  def create_lists(self):
    ''' Create list of files, extensions and file names split on user given character.
        Will overwrite previously created lists. '''

    # Reset lists.
    self.ext_list = [] 
    self.file_list = [] 
    self.file_name_list = []

    choice = input('Would you like to provide a spicific character to generate file names with? (Y/N)'\
                   '\n  Ex. 12345.txt (split on ".") = 12345: ').upper()
  
    while choice != 'Y' and choice != 'N':
      choice = input('That is not a valid answer, please pres "Y" or "N". ').upper()
    
    if choice == 'Y':
      self.split_char = input('Please specify which character you would like to split the name on.' \
                              '\n  Case sensitivity is important ("c" != "C"), the default character is "." : ')
    
    if len(self.split_char) == 0 or self.split_char == None:
      self.split_char = '.'
    print('File names will be generated using the character "{}".'.format(self.split_char))

    for _, __, filenames in os.walk(self.root):
        # Skip hidden files.
        filenames = [f for f in filenames if not f[0] == '.']
        for name in filenames:
          # Check to see if the extension is already in the list of extensions.
          if name.split('.')[-1] not in self.ext_list:
            self.ext_list.append(name.split('.')[-1])
          # Check to see if the generated file name exists in the list of file names.
          if name.split(self.split_char)[0] not in self.file_name_list:
            self.file_name_list.append(name.split(self.split_char)[0].strip())
          # Check to see if the file already exists in the list of found files.
          if name not in self.file_list:
            self.file_list.append(name)
    
    self.file_name_list = sorted(self.file_name_list)
    self.file_list = sorted(self.file_list)
    self.ext_list = sorted(self.ext_list)
    print('-' * 100)
