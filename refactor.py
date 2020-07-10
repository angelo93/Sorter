def get_choice():
    choice = input(
        "Are you sure you want to find and delete all empty directories? (Y/N): "
    ).upper()

    while choice != "Y" and choice != "N":
        choice = input('That is not a valid selection, please press "Y" or "N": ').upper()

    return choice


def del_empty_dirs():
    """ Delete all empty directories and subdirectories
        root_path = path of root folder passed in from menu instance. """

    choice = get_choice()

    if choice == "Y":
        print("Empty directories will be deleted")
    else:
        print("Empty directories will not be deleted.")


del_empty_dirs()
