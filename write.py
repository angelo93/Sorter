def txt_list(list_name, file_name):
  with open(file_name, "w") as text_file:
    for item in list_name:
      text_file.write(item + '\n')

  text_file.close()
