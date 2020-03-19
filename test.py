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
  print(root)