# import os
# import string
# import shutil

# root = os.getcwd() + "/test"
# root_path = root.replace("\\", "/")


people = {
    "1": {"name": "John", "age": "27", "sex": "Male"},
    "2": {"name": "Marie", "age": "22", "sex": "Female"},
    "3": {"name": "Luna", "age": "24", "sex": "Female", "married": "No"},
}

for file_name, file_info in people.items():
    print(file_name + file_info["name"])
