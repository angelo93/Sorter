""" This file stores helper functions. """

import os
import shutil
import string


def make_logs_dir(save_path):
    """ Make the folder to hold text files. """

    try:
        os.mkdir(save_path)
    except FileExistsError:
        print("Folder for logs already exists")


def get_parent_dir_ONBE(file_name):
    """ Determine the parent directory based on a file's name to be organized alphabetically. """

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
    """ Determine the parent directory based on a file's extension to be organized alphabetically. """

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
    """ Create a list of directories to skip. """
    dirs_to_skip = [char for char in string.ascii_uppercase]
    dirs_to_skip.append("#")
    dirs_to_skip.append("Other")

    return dirs_to_skip


def verify(msg):
    print("Are you sure you would like to,")
    choice = input(msg).lower()

    while choice != "y" and choice != "n":
        choice = input("Please choose (y)es or (n)o: ").lower()

    if choice == "y":
        return True
    else:
        return False


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_custom_char_and_index():
    # Get example file name from user
    example_file = input("Please enter a file to use as a template:\n")
    msg = ""
    user_params = []

    verifying = True
    while verifying == True:
        split_char = get_split_char()
        print(
            f"Files will be split like so...\n  {example_file.split(split_char)}")
        print("-" * 50)

        max = len(example_file.split(split_char)) - 1
        index = get_index(max)

        print(
            f"Filenames will be similar to...\n  {example_file.split(split_char)[index]}")
        print("-" * 50)

        msg = f"Use the character '{split_char}' and an index of {index} to sort your files? (y/n) "
        verifying = not verify(msg)

    user_params.append(split_char)
    user_params.append(index)

    return user_params


def get_split_char():
    # Ask which character they would like to split the file name with
    split_char = input(
        "Please provide a character you would like to the split the filename with: ")

    while len(split_char) != 1:
        split_char = input(print("Please choose only ONE character: "))

    return split_char


def get_index(max):
    # Ask for an index to create the files new alias.
    print("Please provide an index to use.")
    index = input(f"Input range is 0 - {max}: ")

    while index.isdigit() == False or int(index) > max:
        index = input("Please provide a number within the range: ")

    return int(index)


def create_data_sets(root_path, edit_params):
    """ Create list of files, extensions and file names split on user given character.
        Will overwrite previously created lists. """

    if len(edit_params[0]) != 1:
        return print("Unable to split filenames with more than or less than one character.")

    data_sets = []

    ext_list = get_ext_list(root_path, deep_dive=True)
    file_list = get_file_list(root_path, deep_dive=True)
    filename_list = get_filename_list(root_path, edit_params, deep_dive=True)
    dup_list = get_file_list(root_path, deep_dive=True, duplicates=True)

    data_sets.append(ext_list)
    data_sets.append(file_list)
    data_sets.append(filename_list)
    data_sets.append(dup_list)

    return data_sets


def get_file_list(root_path, deep_dive=False, duplicates=False):
    """ Create a list of files in a given directory """

    file_list = []
    dup_list = []

    if deep_dive == True:
        for dirpath, _, filenames in os.walk(root_path):
            if dirpath.split("\\")[-1].startswith("."):
                continue
            # Skip hidden files.
            filenames = [f for f in filenames if not f[0] == "."]
            for name in filenames:
                if name not in file_list:
                    file_list.append(name)
                else:
                    dup_list.append(name)

    else:
        for filename in os.listdir(root_path):
            if filename.startswith("."):
                continue
            if os.path.isfile(os.path.join(root_path, filename)):
                file_list.append(filename)

    if duplicates:
        return dup_list
    else:
        return file_list


def get_ext_list(root_path, deep_dive=False):
    """ Create a list of all found extensions """

    ext_list = []

    if deep_dive == True:
        for dirpath, _, filenames in os.walk(root_path):
            if dirpath.split("\\")[-1].startswith("."):
                continue
            # Skip hidden files.
            filenames = [f for f in filenames if not f[0] == "."]
            for name in filenames:
                if name.split(".")[-1] not in ext_list:
                    ext_list.append(name.split(".")[-1])

    else:
        for filename in os.listdir(root_path):
            if filename.startswith("."):
                continue
            if os.path.isfile(os.path.join(root_path, filename)):
                ext_list.append(filename.split(".")[-1])

    return ext_list


def get_filename_list(root_path, edit_params, deep_dive=False):
    """ Create a list of all found extensions """
    if len(edit_params[0]) != 1:
        return print("Unable to split filenames with more than or less than one character.")

    filename_list = []

    if deep_dive == True:
        for dirpath, _, filenames in os.walk(root_path):
            if dirpath.split("\\")[-1].startswith("."):
                continue
            # Skip hidden files.
            filenames = [f for f in filenames if not f[0] == "."]
            for name in filenames:
                if name.split(edit_params[0])[edit_params[1]].strip() not in filename_list:
                    filename_list.append(name.split(edit_params[0])[
                                         edit_params[1]].strip())

    else:
        for filename in os.listdir(root_path):
            if filename.startswith("."):
                continue
            if os.path.isfile(os.path.join(root_path, filename)):
                filename_list.append(filename.split(edit_params[0])[
                                     edit_params[1]].strip())

    return filename_list


def get_all_lists(root_path, edit_params):

    ext_list = []
    file_list = []
    filename_list = []
    dup_list = []
    data_sets = []

    for _, __, filenames in os.walk(root_path):
        # Skip hidden files.
        filenames = [f for f in filenames if not f[0] == "."]
        for name in filenames:
            # Check to see if the extension is already in the list of extensions.
            if name.split(".")[-1] not in ext_list:
                ext_list.append(name.split(".")[-1])
            # Check to see if the generated file name exists in the list of file names.
            if name.split(edit_params[0])[edit_params[1]].strip() not in filename_list:
                filename_list.append(name.split(edit_params[0])[
                                     edit_params[1]].strip())
            # Check to see if the file already exists in the list of found files.
            if name not in file_list:
                file_list.append(name)
            else:
                dup_list.append(name)

    data_sets.append(ext_list)
    data_sets.append(file_list)
    data_sets.append(filename_list)
    data_sets.append(dup_list)

    return data_sets
