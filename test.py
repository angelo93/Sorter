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

print(alpha_dirs)

for dirpath, dirnames, filenames in os.walk(root):
  dirnames[:] = [d for d in dirnames if not d.startswith('.')]
  for dirname in dirnames:
    source = os.path.join(dirpath, dirname).replace('\\', '/')
    if source not in alpha_dirs:
      if dirname[0].isalpha():
        destination = os.path.join(dirpath, dirname[0].upper(), dirname)
        try:
          shutil.move(source, destination)
        except FileNotFoundError:
          print('The destination directory does not exist.')
      elif dirname[0].isdigit():
        destination = os.path.join(dirpath, '#', dirname)
        try:
          shutil.move(source, destination)
        except FileNotFoundError:
          print('The destination directory does not exist.')
      else:
        destination = os.path.join(dirpath, 'Other', dirname)
        try:
          shutil.move(source, destination)
        except FileNotFoundError:
          print('The destination directory does not exist.')