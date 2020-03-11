# Import required libraries
import directory
import write
import move
import os
import sys

class MainMenu:
  """ Class dealing with all main meny functions. """

  def __init__(self):
    self.root = os.getcwd() + '\\test' # The root path directory to be sorted.
    self.files_txt = 'file_list.txt' # Filename for creating a text file of all found files.
    self.exts_txt = 'ext_list.txt' # Filename for creating a text file of all found extensions.
    self.ext_list = [] # List to hold all extensions.
    self.file_list = [] # List to hold all found files.
    self.directory_ext_dict = {} # Dictionary with key as an extension and the value as a directory path.
    self.passes = 0 # Simple variable to check how many times the user has selected an option.

  def create_file_and_ext_lists(self):
    """ Create list of files and extensions found. """

    for dirpath, dirnames, filenames in os.walk(self.root):
        for name in filenames:
          # Check to see if the extension is already in the list of extensions.
          if name.split('.')[-1] not in self.ext_list:
            self.ext_list.append(name.split('.')[-1])
          
          self.file_list.append(name)

  def show_menu(self):
    """ Show main options to user. """
    print('Press 1 to Create a directory for all found extensions')
    print('Press 2 to Create a file listing all found files')
    print('Press 3 to Create a file listing all found extensions')
    print('Press 4 to delete all empty directories')
    print('Press 5 to files to corresponding directories')
    print('Press 6 to terminate program')

  def get_opt(self):
    """ Get option from user. """

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
    """ Execute the chosen option of the user. 
        option = option passed in from user. """

    if option == '1':
      try:
        #Create directories for each extension type in ext_list.
        self.directory_ext_dict = directory.create_directory(self.root, self.ext_list)
        print(self.directory_ext_dict)
      except:
        print('Could not create directories')
    if option == '2':
      # Write list of files to a txt file.
      write.txt_list(self.file_list, self.files_txt)
    if option == '3':
      # Write list of found extensions to txt file.
      write.txt_list(self.ext_list, self.exts_txt)
    if option == '4':
      # Delete all empty directories and subdirectories.
      directory.del_empty_dirs(self.root)
    if option == '5':
      # Move found files to directory corresponding to their extension.
      move.move_files(self.root, self.directory_ext_dict)
    if option == '6':
      print('Terminating program')
      sys.exit()
    if option == 'M':
      self.show_menu()
      
    print('---------------------------------------------------------------------------')
