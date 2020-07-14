import os
import string
import shutil

# root = os.getcwd() + "/test"
# root_path = root.replace("\\", "/")


# CUSTOM SPLIT CHARACTER LOGIC FOR CREATING LISTS
# choice = input(
#     "Would you like to provide a spicific character to generate file names with? (Y/N)"
#     '\n  Ex. 12345.txt (split on ".") = 12345: '
# ).lower()

# while choice != "y" and choice != "n":
#     choice = input(
#         'That is not a valid answer, please press "y" or "n". ').lower()

# if choice == "Y":
#     split_char = input(
#         "Please specify which character you would like to split the name on."
#         '\n  Case sensitivity is important ("c" != "C"), the default character is "." : '
#     )

# if len(split_char) == 0 or split_char == None:
#     split_char = "."

# print('File names will be generated using the character "{}".'.format(
#     split_char))
