#Read files in root directory
#Create a folder for each file extension found if no folder exists already
#Move files into their respective folders

#Import required libraries
import os
import sys
import shutil

#Initialize variables
root_path = "C:/Users/Angel/Desktop/Projects/Main/Sorter/test"
file_list_text = 'file_list.txt'
file_list = []
ext_list_text = 'ext_list.txt'
ext_list = []

#Create a list of files in the root directory
for root, dirs, files in os.walk(root_path):
    for file in files:
      file_list.append(file)

#Create a list of all found extensions
for root, dirs, files in os.walk(root_path):
    for file in files:
      ext_list.append(file.split('.')[-1])

def writeList(list_name, file_name):
  with open(file_name, "w") as text_file:
    for item in list_name:
      text_file.write(item + '\n')

  text_file.close()

writeList(file_list, file_list_text)
writeList(ext_list, ext_list_text)

#Write list of files to a txt file
#Write list of found extensions to txt file