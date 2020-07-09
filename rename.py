import os
import string
import shutil

root_path = 'F:\Comic Library\Artbooks\Staging'
files = []


def rename_extension(root_path, old_ext, new_ext):
    for filename in os.listdir(root_path):
        if os.path.isfile(os.path.join(root_path, filename)):
            files.append(filename)

    for filename in files:
        if filename.split('.')[-1] == old_ext:
            new_filename = filename
            temp = new_filename.split('.')
            temp[-1] = new_ext
            new_filename = '.'.join(temp)
            try:
                os.rename(os.path.join(root_path, filename),
                          os.path.join(root_path, new_filename))
            except:
                print(f'Unable to rename the extension of {filename}.')


rename_extension(root_path, 'rar', 'cbr')
