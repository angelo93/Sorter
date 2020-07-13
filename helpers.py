import os
import shutil
import string


def make_logs_dir(file_name, save_path):
    """ Make the folder to hold text files. """

    try:
        os.mkdir(save_path)
    except FileExistsError:
        print("Folder for lists already exists, proceeding to write {}".format(file_name))
