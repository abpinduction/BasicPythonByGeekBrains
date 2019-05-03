import os


def make_dir(dir_name=None):
    try:
        os.mkdir(dir_name)
        print(f'Folder {dir_name} is successfully created')
    except FileExistsError:
        print(f'Folder {dir_name} is impossible to create')


def remove_dir(dir_name=None):
    try:
        os.rmdir(dir_name)
        print(f'Folder {dir_name} has been successfully deleted')
    except FileNotFoundError:
        print(f'Folder {dir_name} is impossible to find')


def list_dir():
    lst = os.listdir()
    for folder in lst:
        if os.path.isdir(folder):
            print(folder)


def ch_dir(dir_path):
    print('Path to move: ' + dir_path)
    try:
        os.chdir(dir_path)
        print(f'Current folder has been successfully changed to folder {dir_path}')
    except FileNotFoundError:
        print('Folder was not changed')
