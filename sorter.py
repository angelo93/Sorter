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
ext_list_text = 'ext_list.txt'

def createFileList(root_path):
  file_list = []

  #Create a list of files in the root directory
  for root, dirs, files in os.walk(root_path):
      for file in files:
        file_list.append(file)

  return file_list

def creatExtList(root_path):
  ext_list = []

  #Create a list of all found extensions
  for root, dirs, files in os.walk(root_path):
      for file in files:
        ext_list.append(file.split('.')[-1])

  return ext_list

def writeList(list_name, file_name):
  with open(file_name, "w") as text_file:
    for item in list_name:
      text_file.write(item + '\n')

  text_file.close()

def create_directory(root_path, ext_list):
  for ext in ext_list:
    try:
      path = os.path.join(root_path, ext)
      os.mkdir(path)
    except:
      print("Creation of the directory failed")

#Create a list of files and extensions found in directory tree
ext_list = creatExtList(root_path)
file_list = createFileList(root_path)

#Create directories for each extension type in ext_list
create_directory(root_path, ext_list)

#Write list of files to a txt file
# writeList(file_list, file_list_text)
#Write list of found extensions to txt file
# writeList(ext_list, ext_list_text)
