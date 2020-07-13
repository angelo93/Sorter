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
