# Import required libraries
import directory
import write
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
    self.directory_ext_dict, Dictionary with key as an extension and the value as a directory path.
    self.directory_file_name_dict, Dictionary with file name as key and the value as a directory path.
    self.passes, Simple variable to check how many times the user has selected an option.
    self.split_char, Variable to specify which character to split file names on. '''

  def __init__(self, root_path = os.getcwd()):
    self.root = root_path.replace('\\', '/') + '\\test' # The root path directory to be sorted, default is directory where script is located.
    self.files_txt = 'file_list.txt' # Filename for creating a text file of all found files.
    self.exts_txt = 'ext_list.txt' # Filename for creating a text file of all found extensions.
    self.file_name_txt = 'file_name_list.txt' # Filename for creating a text file of all found file names.
    self.ext_list = [] # List to hold all extensions.
    self.file_list = [] # List to hold all found files.
    self.file_name_list = [] # List to hold all found file names.
    self.directory_ext_dict = {} # Dictionary with key as an extension and the value as a directory path.
    self.directory_file_name_dict = {} # Dictionary with file name as key and the value as a directory path.
    self.passes = 0 # Simple variable to check how many times the user has selected an option.
    self.split_char = '' # Variable to specify which character to split file names on.

  def show_menu(self):
    ''' Show main options to user. '''

    print('Press 1 to create directories.')
    print('Press 2 to create txt files.')
    print('Press 3 to delete all empty directories.')
    print('Press 4 to move files to corresponding directories.')
    print('Press 5 to change root directory.')
    print('Press 6 to terminate program.')
    print('-' * 100)

  def get_opt(self):
    ''' Get option from user. '''

    # Check to see if first time called.
    if self.passes == 0:
      option = input('Please select an option: ').upper()
    else:
      print('If you would like to look at the main menu, press "M".')
      option = input('Please select another option: ').upper()

    # List of valid inputs
    valid = ['1', '2', '3', '4', '5', '6', 'M']

    # If option is not a valid option, ask user again.
    while option not in valid:
      print('If you would like to look at the main menu, press "M".')
      option = input('That is not a valid option, please try again: ')
    
    self.passes += 1
    return option

  def execute_opt(self, option):
    ''' Execute the chosen option of the user. 
        option = option passed in from user. '''

    if option == '1':
      # Create directories of a particular type
      self.option_one()
    if option == '2':
      # Write files using generated lists
      self.option_two()
    if option == '3':
      # Delete all empty directories and subdirectories.
      directory.del_empty_dirs(self.root)
    if option == '4':
      # Move found files to directory corresponding to their extension.
      self.option_four()
    if option == '5':
      self.option_five()
    if option == '6':
      print('Terminating program')
      sys.exit()
    if option == 'M':
      self.show_menu()
      
    print('-' * 100)

  def option_one(self):
    ''' Function to decide what kind of directories to create. '''

    print('-' * 100)
    print('Press 1 to create directories for found extensions')
    print('Press 2 to create directories for found file names')
    
    choice = input('Please select an option: ')
    valid = ['1', '2']

    while choice not in valid:
      choice = input('That is not a valid option, please try again: ')
    if choice == '1':
      try:
        #Create directories for each extension type in ext_list.
        self.directory_ext_dict = directory.create_directory_dict(self.root, self.ext_list)
      except:
        print('Could not create directories')
    if choice == '2':
      try:
        #Create directories for each file name in file_name_list.
        self.directory_file_name_dict = directory.create_directory_dict(self.root, self.file_name_list)
      except:
        print('Could not create directories')
  
  def option_two(self):
    ''' Create a file listing either all
          extensions, files and or file names. '''

    print('-' * 100)
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
      write.txt_list(self.file_list, self.files_txt)
    if choice == '2':
      # Write list of found extensions to txt file.
      write.txt_list(self.ext_list, self.exts_txt)
    if choice == '3':
      # Write list of found extensions to txt file.
      write.txt_list(self.file_name_list, self.file_name_txt)
    if choice == '4':
      # Write all files from above options
      write.txt_list(self.file_list, self.files_txt)
      write.txt_list(self.ext_list, self.exts_txt)
      write.txt_list(self.file_name_list, self.file_name_txt)

  def option_four(self):
    ''' Decide whether user is moving files based on their extensions or names
        and would also like to organize directories into alphabetical folders. '''

    print('-' * 100)
    print('Press 1 to move files based on their extensions')
    print('Press 2 to move files based on their names')

    choice = input('Please select an option: ')
    valid = ['1', '2']

    while choice not in valid:
      choice = input('That is not a valid option, please try again: ')
    if choice == '1':
      directory.move_files(self.root, self.directory_ext_dict, choice)
    if choice == '2':
      directory.move_files(self.root, self.directory_file_name_dict, choice, self.split_char)

    org_dirs = input('Would you like to organize the directories into alphabetical folders? (Y/N): ').upper()

    while org_dirs != 'Y' and org_dirs != 'N':
      org_dirs = input('Please press "Y" or "N" to organize directories into alphabetical folders: ').upper()

    if org_dirs == 'Y':
      directory.org_by_alpha(self.root)
  
  def option_five(self):
    ''' Change root directory path and reset file, extension and file name lists.'''

    # Get new path from user.
    new_dir_path = input('Please provide the new root directory path:\n')

    # Check to see if new path exists, 
    if os.path.isdir(new_dir_path): # If yes, change current to root to new root and create new lists.
      self.root = new_dir_path.replace('\\', '/')
      self.create_lists()
    else:
      print('That directory does not exist.')

  def create_lists(self):
    ''' Create list of files, extensions and file names split on user given character.
        Will overwright previously created lists. '''

    # Reset lists.
    self.ext_list = [] 
    self.file_list = [] 
    self.file_name_list = []

    choice = input('Would you also like to create a lists of file names split on a specified character? (Y/N)'\
                    '\n  Ex. 12345[213123].txt split on "[" = 12345: ').upper()
  
    while choice != 'Y' and choice != 'N':
      choice = input('That is not a valid answer, please pres "Y" or "N". ')
    
    if choice == 'Y':
      self.split_char = input('Please specify which character you would like to split the name on.' \
                          '\n  Case sensitivity is important ("c" != "C"): ')
      print('File names will be split using "{}".'.format(self.split_char))
      for _, __, filenames in os.walk(self.root):
        # Skip hidden files.
        filenames = [f for f in filenames if not f[0] == '.']
        for name in filenames:
          if name.split(self.split_char)[0] not in self.file_name_list:
            self.file_name_list.append(name.split(self.split_char)[0])
      self.file_name_list = sorted(self.file_name_list)

    for _, __, filenames in os.walk(self.root):
        # Skip hidden files.
        filenames = [f for f in filenames if not f[0] == '.']
        for name in filenames:
          # Check to see if the extension is already in the list of extensions.
          if name.split('.')[-1] not in self.ext_list:
            self.ext_list.append(name.split('.')[-1])
          self.file_list.append(name)
    
    self.file_list = sorted(self.file_list)
    self.ext_list = sorted(self.ext_list)
    print('-' * 100)
