""" This file stores all helper functions. """

# Import required libraries
import os
import shutil
import string


def del_empty_dirs(root_path):
    """ Delete all empty directories and subdirectories
        root_path = path of root folder passed in from menu instance. """

    choice = input(
        "Are you sure you want to find and delete all empty directories? (Y/N): "
    ).upper()
    deleted_dirs = []  # List to record deleted directories
    deleted_txt = "deleted_dirs.txt"  # Text file to view deleted directories

    while choice != "Y" and choice != "N":
        choice = input('That is not a valid selection, please press "Y" or "N": ').upper()

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


def move_files(root_path, split_char=".", index=-1, organize=False, by_ext=True):
    parent = ""

    dirs_to_skip = [char for char in string.ascii_uppercase]
    dirs_to_skip.append("#")
    dirs_to_skip.append("Other")

    for dirpath, _, filenames in os.walk(root_path):
        # Skip hidden directories.
        if dirpath.split("\\")[-1].startswith(".") or dirpath.split("\\")[-1] in dirs_to_skip:
            continue
        for name in filenames:
            # Skip hidden files.
            if name.startswith("."):
                continue
            # If organizing by file name, set parent to...
            if organize and not by_ext:
                # Check to see if file name starts with a number.
                if name[0].isdigit():
                    parent = "#"
                # Check to see if file name starts with a letter.
                elif name[0].isalpha():
                    parent = name[0].upper()
                else:  # If file name doesn't start with a number or a letter.
                    parent = "Other"
            # If organizing by file extension, set parent to...
            elif organize and by_ext:
                # Check to see if extension starts with a number.
                if name.split(split_char)[index][0].isdigit():
                    parent = "#"
                # Check to see if extension starts with a letter.
                elif name.split(split_char)[index][0].isalpha():
                    parent = name.split(split_char)[index][0].upper()
                else:  # If extension starts with anything else.
                    parent = "Other"
            # If split_char == '.', file's extension otherwise file's name
            current_file = name.split(split_char)[index].strip()
            # Source path of current file.
            source = os.path.join(dirpath, name).replace("\\", "/")
            destination = os.path.join(root_path, parent, current_file, name).replace("\\", "/")
            # Check to see if the file needs to be moved, if not continue to next file.
            if source == destination:
                continue
            # Makes the necessary directories for the destination. If they already exist, move the file.
            try:
                os.makedirs(os.path.join(root_path, parent, current_file), exist_ok=True)
                shutil.move(source, destination)
            except FileExistsError:
                print('The file "{}" already exists.'.format(destination))
            except FileNotFoundError:
                print('Source "{}" does not exist'.format(source))


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
