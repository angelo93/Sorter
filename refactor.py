import os
import shutil
import string


def move_files(root_path, split_char=".", index=-1, organize=False, by_ext=True):
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
        for name in filenames:
            # Skip hidden files.
            if name.startswith("."):
                continue

            # If organizing by file name, set parent directory to...
            if organize and not by_ext:
                # Check to see if file name starts with a number.
                if name[0].isdigit():
                    parent_dir = "#"
                # Check to see if file name starts with a letter.
                elif name[0].isalpha():
                    parent_dir = name[0].upper()
                else:  # If file name doesn't start with a number or a letter.
                    parent_dir = "Other"

            # If organizing by file extension, set parent directory to...
            elif organize and by_ext:
                # Check to see if extension starts with a number.
                if name.split(split_char)[index][0].isdigit():
                    parent_dir = "#"
                # Check to see if extension starts with a letter.
                elif name.split(split_char)[index][0].isalpha():
                    parent_dir = name.split(split_char)[index][0].upper()
                else:  # If extension starts with anything else.
                    parent_dir = "Other"

            # If split_char == '.', file's extension otherwise file's name
            current_file = name.split(split_char)[index].strip()

            # Source path of current file.
            source = os.path.join(dirpath, name).replace("\\", "/")
            destination = os.path.join(
                root_path, parent_dir, current_file, name).replace("\\", "/")

            # Check to see if the file needs to be moved, if not continue to next file.
            if source == destination:
                continue

            # Makes the necessary directories for the destination. If they already exist, move the file.
            try:
                os.makedirs(os.path.join(root_path, parent_dir,
                                         current_file), exist_ok=True)
                shutil.move(source, destination)
            except FileExistsError:
                print('The file "{}" already exists.'.format(destination))
            except FileNotFoundError:
                print('Source "{}" does not exist'.format(source))
