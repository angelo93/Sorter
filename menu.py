import directory
import write
import move
import os

class MainMenu:
  def __init__(self):
    self.root = os.getcwd() + '\\test'
    self.files_txt = 'file_list.txt'
    self.exts_txt = 'ext_list.txt'
    self.ext_list = []
    self.file_list = []
    self.directory_ext_dict = {}
    self.passes = 0

  def create_file_and_ext_lists(self):
    #Create a list of files in the root directory
    for dirpath, dirnames, filenames in os.walk(self.root):
        for name in filenames:
          if name.split('.')[-1] not in self.ext_list:
            self.ext_list.append(name.split('.')[-1])
          self.file_list.append(name)
    # Remove duplicates in list of extensions 
    # self.ext_list = set(self.ext_list)

  def show_menu(self):
    print('Press 1 to Create a directory for all found extensions')
    print('Press 2 to Create a file listing all found files')
    print('Press 3 to Create a file listing all found extensions')
    print('Press 4 to delete all empty directories')
    print('Press 5 to files to corresponding directories')
    print('Press 6 to terminate program')

  def get_opt(self):
    if self.passes == 0:
      option = input('Please select an option: ').upper()
    else:
      option = input('Please select another option: ').upper()
      print('If you would like to look at the main menu, press "M".')

    valid = ['1', '2', '3', '4', '5', '6', 'M']

    while option not in valid:
      option = input('That is not a valid option, please try again: ')
    
    self.passes += 1
    return option

  def execute_opt(self, option):
    if option == '1':
      try:
        #Create directories for each extension type in ext_list
        self.directory_ext_dict = directory.create_directory(self.root, self.ext_list)
      except:
        print('Could not create directories')
    if option == '2':
      # Write list of files to a txt file
      write.txt_list(self.file_list, self.files_txt)
    if option == '3':
      # Write list of found extensions to txt file
      write.txt_list(self.ext_list, self.exts_txt)
    if option == '4':
      directory.del_empty_dirs(self.root)
    if option == '5':
      move.move_files(self.root, self.directory_ext_dict)
    if option == '6':
      print('Terminating program')
    
    print('---------------------------------------------------------------------------')
