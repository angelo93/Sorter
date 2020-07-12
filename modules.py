""" This file stores all helper functions. """

# Import required libraries
import os
import shutil
import string


def del_empty_dirs(root_path):
    """ Delete all empty directories and subdirectories
        root_path = path of root folder passed in from menu instance. """

    def get_choice():
        choice = input(
            "Are you sure you want to find and delete all empty directories? (Y/N): "
        ).upper()

        while choice != "Y" and choice != "N":
            choice = input('That is not a valid selection, please press "Y" or "N": ').upper()

        return choice

    choice = get_choice()
    deleted_dirs = []  # List to record deleted directories
    deleted_txt = "deleted_dirs.txt"  # Text file to view deleted directories

    if choice == "Y":
        for dirpath, dirnames, _ in os.walk(root_path, topdown=False):
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            try:
                os.rmdir(dirpath)
                deleted_dirs.append(dirpath)
            except:
                print("{} is not empty".format(dirpath))

        if len(deleted_dirs) > 0:
            print("All empty directories have been deleted")
            print(
                "If you would like to review the directories deleted, please review the deleted_dirs.txt file"
            )
            write_txt_list(deleted_dirs, deleted_txt)
        else:
            print("There were no empty directories to delete")
    else:
        print("Empty directories will not be deleted.")


def create_file_dictionary(root_path, split_char=".", index=-1, organize=False, by_ext=True):
    dirs_to_skip = []
    file_dictionary = {}
    parent_dir = ""

    # Helper function to create list of dirs to skip.
    def get_dirs_to_skip():
        dirs_to_skip = [char for char in string.ascii_uppercase]
        dirs_to_skip.append("#")
        dirs_to_skip.append("Other")

        return dirs_to_skip

    dirs_to_skip = get_dirs_to_skip()

    for dirpath, _, filenames in os.walk(root_path):
        # Skip hidden directories & aformentioned dirs to skip.
        if dirpath.split("\\")[-1].startswith(".") or dirpath.split("\\")[-1] in dirs_to_skip:
            continue

        for file_name in filenames:
            # If split_char == '.', file's extension otherwise file's name w/out extension
            current_file_alias = file_name.split(split_char)[index].strip()

            # Skip hidden files.
            if file_name.startswith("."):
                continue

            # If organizing by file name, set parent directory to...
            if organize and not by_ext:
                parent_dir = get_parent_dir_ONBE(file_name) + "\\" + current_file_alias
                destination = os.path.join(root_path, parent_dir, file_name).replace("\\", "/")

            # If organizing by file extension, set parent directory to...
            elif organize and by_ext:
                parent_dir = get_parent_dir_OBE(file_name, split_char, index) + "\\" + current_file_alias
                destination = os.path.join(root_path, parent_dir, file_name).replace("\\", "/")

            else:
                parent_dir = current_file_alias
                destination = os.path.join(root_path, current_file_alias, file_name).replace("\\", "/")

            # Source path of current file.
            source = os.path.join(dirpath, file_name).replace("\\", "/")

            file_dictionary[file_name] = {
                "parent_dir": parent_dir,
                "source": source,
                "destination": destination,
            }

    return file_dictionary


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


def move_files(root_path, file_dictionary):
    for _, file_info in file_dictionary.items():
        # Check to see if the file needs to be moved, if not continue to next file.
        if file_info["source"] == file_info["destination"]:
            continue

        try:
            os.makedirs(os.path.join(root_path, file_info["parent_dir"]), exist_ok=True)
            shutil.move(file_info["source"], file_info["destination"])
        except FileExistsError:
            print('The file "{}" already exists.'.format(file_info["destination"]))
        except FileNotFoundError:
            print('Source "{}" does not exist'.format(file_info["source"]))


def write_txt_list(list_name, file_name):
    """ Record elements in a given list to a text file for reference. """

    def make_logs_dir(file_name):
        """ Make the folder to hold text files. """
        try:
            os.mkdir(save_path)
        except FileExistsError:
            print("Folder for lists already exists, proceeding to write {}".format(file_name))

    save_path = os.getcwd() + "\\logs"

    # Create the complete path name for the text file.
    complete_name = os.path.join(save_path, file_name)

    # Call make_dir to make the text folder in case it's not present.
    make_logs_dir(file_name)

    with open(complete_name, "w", encoding="utf-8") as text_file:
        for item in list_name:
            text_file.write(item + "\n")

    text_file.close()


def rename_extension(root_path, old_ext, new_ext):
    filenames = []

    for filename in os.listdir(root_path):
        if os.path.isfile(os.path.join(root_path, filename)):
            filenames.append(filename)

    for filename in filenames:
        if filename.split(".")[-1] == old_ext:
            new_filename = filename
            temp = new_filename.split(".")
            temp[-1] = new_ext
            new_filename = ".".join(temp)
            try:
                os.rename(os.path.join(root_path, filename), os.path.join(root_path, new_filename))
            except:
                print(f"Unable to rename the extension of {filename}.")
