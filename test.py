import os
import string
import shutil

root = os.getcwd() + '/test'
root_path = root.replace('\\', '/')


def move_files(root_path, split_char='.', index=-1, organize=False):
    parent = ''

    dirs_to_skip = [char for char in string.ascii_uppercase]
    dirs_to_skip.append('#')
    dirs_to_skip.append('Other')

    for dirpath, _, filenames in os.walk(root_path):
        # Skip hidden directories.
        if dirpath.split('\\')[-1].startswith('.') or dirpath.split('\\')[-1] in dirs_to_skip:
            continue
        for name in filenames:
            # Skip hidden files.
            if name.startswith('.'):
                continue
            if organize:
                if name[0].isdigit():
                    parent = '#'
                elif name[0].isalpha():
                    parent = name[0].upper()
                else:
                    parent = 'Other'

            # If split_char == '.', file's extension otherwise file's name
            current_file = name.split(split_char)[index].strip()
            # Source path of current file.
            source = os.path.join(dirpath, name).replace('\\', '/')
            destination = os.path.join(
                root_path, parent, current_file, name).replace('\\', '/')
            try:
                shutil.move(source, destination)
            except FileExistsError:
                print('The file "{}" already exists.'.format(destination))
            except FileNotFoundError:
                print('Source "{}" does not exist'.format(source))


move_files(root_path)
