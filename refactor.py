import os
import shutil
import string
import helpers
import modules

# test


def option_one(log_data_sets, log_names):
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

    index = 0
    for data_set in log_data_sets:
        modules.write_logs(data_set, log_names[index])
        index += 1

    if choice == "Q":
        helpers.clear_screen()
        self.show_menu()
        return

    print("-" * 100)
