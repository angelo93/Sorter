import os

root = os.getcwd()

# for dirpath, dirnames, filenames in os.walk(root):

#   dirnames[:] = [d for d in dirnames if not d.startswith('.')]

#   for dirname in dirnames:
#     print(os.path.join(dirpath, dirname))

for dirpath, dirnames, files in os.walk(root):
  dirnames[:] = [d for d in dirnames if not d.startswith('.')]
  for dirname in dirnames:
    source = os.path.join(dirpath, dirname)
    if dirname[0].isalpha():
      destination = os.path.join(dirpath, '#', dirname)
      print(source, destination)