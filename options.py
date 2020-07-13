import modules
import helpers
import os


def option_one(log_info, log_name):
    """ Create a file listing either all
          extensions, files and or file names. """

    print("Press 1 to create a log listing all extensions.")
    print("Press 2 to create a log listing all files.")
    print("Press 3 to create a log listing all file names.")
    print("Press 4 to create a log listing all duplicate files.")
    print("Press 5 to create all logs.")
    print('Press "Q" to go back to Main Menu.')

    choice = input("Please select an option: ").upper()
    valid = ["1", "2", "3", "4", "5", "Q"]

    while choice not in valid:
        choice = input("That is not a valid option, please try again: ")

    if choice == "1":
        # Write list of files to a txt file.
        modules.write_logs(file_list, files_txt)
    if choice == "2":
        # Write list of found extensions to txt file.
        modules.write_logs(ext_list, exts_txt)
    if choice == "3":
        # Write list of found extensions to txt file.
        modules.write_logs(file_name_list, file_name_txt)
    if choice == "4":
        # Write list of found duplicate files to txt file.
        modules.write_logs(dup_list, dup_files_txt)
    if choice == "5":
        # Write all files from above options
        modules.write_logs(file_list, files_txt)
        modules.write_logs(ext_list, exts_txt)
        modules.write_logs(file_name_list, file_name_txt)
        modules.write_logs(dup_list, dup_files_txt)
    if choice == "Q":
        helpers.clear_screen()
        self.show_menu()
        return

    print("-" * 100)


def option_three(self):
    """ Decide whether user is moving files based on their extensions or names
        and would also like to organize directories into alphabetical folders. """

    print("Press 1 to move files based on their extensions")
    print("Press 2 to move files based on their names")

    choice = input("Please select an option: ")
    valid = ["1", "2"]

    while choice not in valid:
        choice = input("That is not a valid option, please try again: ")

    org_dirs = input(
        "Would you like to organize the directories into alphabetical folders? (Y/N): "
    ).upper()

    while org_dirs != "Y" and org_dirs != "N":
        org_dirs = input(
            'Please press "Y" or "N" to organize directories into alphabetical folders: '
        ).upper()

    if org_dirs == "Y":
        print(
            "It is recommended that you delete all current empty directories before organizing to avoid errors."
        )
        modules.del_empty_dirs(self.root)

    if choice == "1" and org_dirs == "Y":
        file_dictionary = modules.create_file_dictionary(
            self.root, organize=True)
    elif choice == "2" and org_dirs == "Y":
        file_dictionary = modules.create_file_dictionary(
            self.root, self.split_char, 0, organize=True, by_ext=False
        )
    elif choice == "1" and org_dirs == "N":
        file_dictionary = modules.create_file_dictionary(self.root)
    else:
        file_dictionary = modules.create_file_dictionary(
            self.root, self.split_char, 0, by_ext=False
        )

    modules.move_files(self.root, file_dictionary)

    print("-" * 100)


def option_four(self):
    """ Change root directory path and reset file, extension and file name lists."""

    # Get new path from user.
    new_dir_path = input("Please provide the new root directory path:\n")

    # Check to see if new path exists,
    # If yes, change current to root to new root and create new lists.
    if os.path.isdir(new_dir_path):
        self.root = new_dir_path.replace("\\", "/")
        self.create_lists()
    else:
        print("That directory {} does not exist.".format(new_dir_path))


def option_five(self):
    """ Batch edit filename extensions in a given folder. """
    print(
        "This will rename all filename extensions in a given folder to a new extension. \n\
      Example: old_file.txt --> new_file.rar."
    )

    root_path = input("Please provide the path for the directory: ")
    old_ext = input(
        'Please provide the extension you wish to replace without the ".": ')
    new_ext = input(
        'Please provide the new extension to be used without the ".": ')

    modules.rename_extension(root_path, old_ext, new_ext)


def create_lists(self):
    """ Create list of files, extensions and file names split on user given character.
        Will overwrite previously created lists. """

    # Reset lists.
    self.ext_list = []
    self.file_list = []
    self.file_name_list = []

    choice = input(
        "Would you like to provide a spicific character to generate file names with? (Y/N)"
        '\n  Ex. 12345.txt (split on ".") = 12345: '
    ).lower()

    while choice != "y" and choice != "n":
        choice = input(
            'That is not a valid answer, please press "y" or "n". ').lower()

    if choice == "y":
        self.split_char = input(
            "Please specify which character you would like to split the name on."
            '\n  Case sensitivity is important ("c" != "C"), the default character is "." : '
        )

    if len(self.split_char) == 0 or self.split_char == None:
        self.split_char = "."

    print('File names will be generated using the character "{}".'.format(
        self.split_char))

    for _, __, filenames in os.walk(self.root):
        # Skip hidden files.
        filenames = [f for f in filenames if not f[0] == "."]
        for name in filenames:
            # Check to see if the extension is already in the list of extensions.
            if name.split(".")[-1] not in self.ext_list:
                self.ext_list.append(name.split(".")[-1])
            # Check to see if the generated file name exists in the list of file names.
            if name.split(self.split_char)[0].strip() not in self.file_name_list:
                self.file_name_list.append(
                    name.split(self.split_char)[0].strip())
            # Check to see if the file already exists in the list of found files.
            if name not in self.file_list:
                self.file_list.append(name)
            else:
                self.dup_list.append(name)

    self.file_name_list = sorted(self.file_name_list)
    self.file_list = sorted(self.file_list)
    self.ext_list = sorted(self.ext_list)
    print("-" * 100)
