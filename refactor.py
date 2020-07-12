import os
import shutil
import string


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
            # If split_char == '.', file's extension otherwise file's name
            current_file = file_name.split(split_char)[index].strip()

            # Skip hidden files.
            if file_name.startswith("."):
                continue

            # If organizing by file name, set parent directory to...
            if organize and not by_ext:
                parent_dir = get_parent_dir_ONBE(file_name) + "\\" + current_file
                destination = os.path.join(root_path, parent_dir, file_name).replace("\\", "/")

            # If organizing by file extension, set parent directory to...
            elif organize and by_ext:
                parent_dir = get_parent_dir_OBE(file_name, split_char, index) + "\\" + current_file
                destination = os.path.join(root_path, parent_dir, file_name).replace("\\", "/")

            else:
                parent_dir = current_file
                destination = os.path.join(root_path, current_file, file_name).replace("\\", "/")

            # Source path of current file.
            source = os.path.join(dirpath, file_name).replace("\\", "/")

            file_dictionary[file_name] = {
                "parent_dir": parent_dir,
                "source": source,
                "destination": destination,
            }

    return file_dictionary


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

