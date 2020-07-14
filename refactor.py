import os
import shutil
import string
import helpers
import modules
import test

root = os.getcwd() + "\\test"
root_path = root.replace("\\", "/")


def option_one():
    """ Create a file listing either all
          extensions, files and or file names. """

    print("Press 1 to create a log listing all extensions.")
    print("Press 2 to create a log listing all files.")
    print("Press 3 to create a log listing all file names.")
    print("Press 4 to create a log listing all duplicate files.")
    print("Press 5 to create all logs.")
    print('Press "Q" to go back to Main Menu.')

    choice = input("Please select an option: ").lower()
    valid = ["1", "2", "3", "4", "5", "q"]

    while choice not in valid:
        choice = input("That is not a valid option, please try again: ")

    if choice == "q":
        helpers.clear_screen()
        # self.show_menu()
        return

    index = int(choice)
    edit_params = test.get_custom_char_and_index()
    data_sets = test.create_data_sets(edit_params, root)
    log_names = ["extension_list.txt", "file_list.txt",
                 "filename_list.txt", "duplicate_files.txt"]

    if index == 5:
        index = 0
        for data_set in data_sets:
            modules.write_logs(data_set, log_names[index])
            index += 1
    else:
        modules.write_logs(data_sets[index - 1], log_names[index - 1])

    print("-" * 100)

