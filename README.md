# **AUTOMATION SCRIPT UTILIZING PYTHON**

#### DESCRIPTION:

A small script to automate the organization of files and folders in a given directory.

Current features include:

- Creation of directories based on extension or file name.
  - File name is generated based on user given character to split file name on. Default value is ".".
  - "1234.txt" --> "1234".
- Deletion of empty directories.
  - Directories are deleted from bottom of tree to top.
- Moving files to a corresponding directory based on their extension or their file name.
- Organization of directories alphabetically.
  - /a_directory, /ab_directory, /abc_directory --> /A/a_directory, /A/ab_directory, /A/abc_directory

#### TO DO:

- [x] - ~~Read in all files in given root directory.~~
- [x] - ~~Record all files found and write to a txt file as a log.~~
- [x] - ~~Implement a UI.~~
- [x] - ~~Implement ability to creat directories based on file name or extension.~~
- [x] - ~~Implement the moving of files into directory based on their name or extension.~~
- [x] - ~~Allow user to delete empty directories/subdirectories and log the deleted directories for reference.~~
- [x] - ~~Implement ability to allow user to specify a character to split file names on.~~
- [x] - ~~Implement option to change root directory.~~
- [x] - ~~Add feature to organize directories alphabetically.~~
- [ ] - Add GUI for easier usability.
- [ ] - Refactor, refactor, refactor.
