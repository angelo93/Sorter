import os
import shutil
import string
import helpers


def write_txt_list(list_name, file_name):
    """ Record elements in a given list to a text file for reference. """

    save_path = os.getcwd() + "\\logs"

    # Create the complete path name for the text file.
    complete_name = os.path.join(save_path, file_name)

    # Call make_dir to make the text folder in case it's not present.
    helpers.make_logs_dir(file_name, save_path)

    with open(complete_name, "w", encoding="utf-8") as text_file:
        for item in list_name:
            text_file.write(item + "\n")

    text_file.close()
