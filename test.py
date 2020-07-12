# import os
# import string
# import shutil

# root = os.getcwd() + "/test"
# root_path = root.replace("\\", "/")

file_one = "something[000][aj][v0].nsp"
file_two = "test.txt"

print(file_one.split("[")[-1].strip())
print(file_two.split("[")[-1].strip())

