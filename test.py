import os

root = os.getcwd()

for dirpath, dirnames, filenames in os.walk(root):

  dirnames[:] = [d for d in dirnames if not d.startswith('.')]

  for dirname in dirnames:
    print(os.path.join(dirpath, dirname))