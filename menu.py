# Import required libraries
import directory
import write
import os
import sys
import shutil

class MainMenu:
  """ Class dealing with all main menu functions. """

  def __init__(self):
    self.root = os.getcwd() + '\\test' # The root path directory to be sorted.
    self.files_txt = 'file_list.txt' # Filename for creating a text file of all found files.
    self.exts_txt = 'ext_list.txt' # Filename for creating a text file of all found extensions.
    self.file_name_txt = 'file_name_list.txt' # Filename for creating a text file of all found file names.
    self.ext_list = [] # List to hold all extensions.
    self.file_list = [] # List to hold all found files.
    self.file_name_list = [] # List to hold all found file names.
    self.directory_ext_dict = {} # Dictionary with key as an extension and the value as a directory path.
    self.directory_file_name_dict = {} # Dictionary with file name as key and the value as a directory path.
    self.passes = 0 # Simple variable to check how many times the user has selected an option.

  def create_lists(self):
    """ Create list of files, extensions and file names split on user given character. """
    split_char = input('Please specify which character you would like to split the name on: ')

    for _, __, filenames in os.walk(self.root):
        for name in filenames:
          # Check to see if the extension is already in the list of extensions.
          if name.split('.')[-1] not in self.ext_list:
            self.ext_list.append(name.split('.')[-1])
          if name.split(split_char)[0] not in self.file_name_list:
            self.file_name_list.append(name.split(split_char)[0])
          self.file_list.append(name)
    
    self.file_list = sorted(self.file_list)
    self.ext_list = sorted(self.ext_list)
    self.file_name_list = sorted(self.file_name_list)

  def show_menu(self):
    """ Show main options to user. """
    print('Press 1 to Create a directories')
    print('Press 2 to Create txt files')
    print('Press 3 to delete all empty directories')
    print('Press 4 to move files to corresponding directories')
    print('Press 5 to terminate program')

  def get_opt(self):
    """ Get option from user. """
    # Check to see if first time called.
    if self.passes == 0:
      option = input('Please select an option: ').upper()
    else:
      print('If you would like to look at the main menu, press "M".')
      option = input('Please select another option: ').upper()

    # List of valid inputs
    valid = ['1', '2', '3', '4', '5', 'M']

    # If option is not a valid option, ask user again.
    while option not in valid:
      print('If you would like to look at the main menu, press "M".')
      option = input('That is not a valid option, please try again: ')
    
    self.passes += 1

    return option

  def option_one(self):
    ''' Function to decide what kind of directories to create. '''
    print('Press 1 to create directories for found extensions')
    print('Press 2 to create directories for found file names')
    
    choice = input('Please select and option: ')
    valid = ['1', '2']

    while choice not in valid:
      choice = input('That is not a valid option, please try again: ')
    
    if choice == '1':
      try:
        #Create directories for each extension type in ext_list.
        self.directory_ext_dict = directory.create_directory(self.root, self.ext_list)
      except:
        print('Could not create directories')
    if choice == '2':
      try:
        #Create directories for each file name in file_name_list.
        self.directory_file_name_dict = directory.create_directory(self.root, self.file_name_list)
      except:
        print('Could not create directories')
  
  def option_two(self):
    ''' Create a file listing either all
          extensions, files and or file names. '''
    print('Press 1 to create a file listing all extensions')
    print('Press 2 to create a file listing all files')
    print('Press 3 to create a file listing all file names')
    
    choice = input('Please select and option: ')
    valid = ['1', '2', '3']

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

  def execute_opt(self, option):
    """ Execute the chosen option of the user. 
        option = option passed in from user. """
    if option == '1':
      self.option_one()
    if option == '2':
      self.option_two()
    if option == '3':
      # Delete all empty directories and subdirectories.
      directory.del_empty_dirs(self.root)
    if option == '4':
      # Move found files to directory corresponding to their extension.
      directory.move_files(self.root, self.directory_ext_dict)
    if option == '5':
      print('Terminating program')
      sys.exit()
    if option == 'M':
      self.show_menu()
      
    print('---------------------------------------------------------------------------')
