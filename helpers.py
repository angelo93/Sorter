import os
import shutil
import string


def make_logs_dir(save_path):
    """ Make the folder to hold text files. """

    try:
        os.mkdir(save_path)
    except FileExistsError:
        print("Folder for logs already exists")


def get_file_list(root_path):
    """ Create a list of files in a given directory """

    file_list = []

    for filename in os.listdir(root_path):
        if os.path.isfile(os.path.join(root_path, filename)):
            file_list.append(filename)

    return file_list


def get_parent_dir_ONBE(file_name):
    parent_dir = ""

    # Check to see if file name starts with a number.
    if file_name[0].isdigit():
        parent_dir = "#"
    # Check to see if file name starts with a letter.
    elif file_name[0].isalpha():
        parent_dir = file_name[0].upper()
    else:  # If file name doesn't start with a number or a letter.
        parent_dir = "Other"

    return parent_dir


def get_parent_dir_OBE(file_name, split_char, index):
    parent_dir = ""

    # Check to see if extension starts with a number.
    if file_name.split(split_char)[index][0].isdigit():
        parent_dir = "#"
    # Check to see if extension starts with a letter.
    elif file_name.split(split_char)[index][0].isalpha():
        parent_dir = file_name.split(split_char)[index][0].upper()
    else:  # If extension starts with anything else.
        parent_dir = "Other"

    return parent_dir


def get_dirs_to_skip():
    """ Helper function to create list of dirs to skip. """
    dirs_to_skip = [char for char in string.ascii_uppercase]
    dirs_to_skip.append("#")
    dirs_to_skip.append("Other")

    return dirs_to_skip
