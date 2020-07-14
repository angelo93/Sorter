import os
import shutil
import string
import helpers
import modules
import test

root = os.getcwd() + "\\test"
root_path = root.replace("\\", "/")


def create_data_sets(root_path, edit_params):
    """ Create list of files, extensions and file names split on user given character.
        Will overwrite previously created lists. """

    if len(edit_params[0]) != 1:
        return print("Unable to split filenames with more than or less than one character.")

    # Reset lists.
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
                filename_list.append(
                    name.split(edit_params[0])[edit_params[1]].strip())
            # Check to see if the file already exists in the list of found files.
            if name not in file_list:
                file_list.append(name)
            else:
                dup_list.append(name)

    ext_list = sorted(ext_list)
    data_sets.append(ext_list)

    file_list = sorted(file_list)
    data_sets.append(file_list)

    filename_list = sorted(filename_list)
    data_sets.append(filename_list)

    if dup_list:
        dup_list = sorted(dup_list)
    data_sets.append(dup_list)

    return data_sets


def get_file_list(root_path):
    """ Create a list of files in a given directory """

    file_list = []

    for filename in os.listdir(root_path):
        # Skip hidden files.
        filenames = [f for f in filenames if not f[0] == "."]
        if os.path.isfile(os.path.join(root_path, filename)):
            file_list.append(filename)

    return file_list
