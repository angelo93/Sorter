import os
import string
import shutil

root = os.getcwd() + '/test'
root = root.replace('\\', '/')

alpha_dirs = [
  root + '/' + '#',
  root + '/' + 'Other'
]

for letter in string.ascii_uppercase:
  alpha_dirs.append(root + '/' + letter)

for dirpath, dirnames, filenames in os.walk(root):
  dirnames[:] = [
    d for d in dirnames if not d.startswith('.') and 
    d[0] not in string.ascii_uppercase and 
    d != '#' and 
    d != 'Other'
  ]
  for dirname in dirnames:
    source = os.path.join(dirpath, dirname).replace('\\', '/')
    if dirname[0].isalpha():
      destination = (dirpath + '/' + dirname[0].upper() + '/' + dirname).replace('\\', '/')
      try:
        shutil.move(source, destination)
      except FileNotFoundError:
        print('The destination directory does not exist.')
    elif dirname[0].isdigit():
      destination = os.path.join(dirpath, dirname).replace('\\', '/')
      try:
        shutil.move(source, destination)
      except FileNotFoundError:
        print('The destination directory does not exist.')
    else:
      destination = os.path.join(dirpath, dirname).replace('\\', '/')
      try:
        shutil.move(source, destination)
      except FileNotFoundError:
        print('The destination directory does not exist.')
    print(destination)