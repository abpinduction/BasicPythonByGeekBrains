import os
import sys
from shutil import copyfile

print(sys.argv)


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def make_dir():
    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), 'dir_' + str(i))
        try:
            os.mkdir(dir_path)
            print(f'Folder dir_{i} is successfully created')
        except FileExistsError:
            print(f'Folder dir_{i} is exist')


def remove_dir():
    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), 'dir_' + str(i))
        try:
            os.rmdir(dir_path)
            print(f'Folder dir_{i} has been successfully deleted')
        except FileNotFoundError:
            print(f'Folder dir_{i} is not found')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir():
    lst = os.listdir()
    for folder in lst:
        if os.path.isdir(folder):
            print(folder)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file():
    file_name = 'easy_05.py'
    new_file_name = 'copy_' + file_name
    if not os.path.isfile(new_file_name):  # если файл с таким именем не существует, тогда копируем
        copyfile(file_name, new_file_name)
    if os.path.exists(new_file_name):  # файл скопирован успешно?
        print(f'File {file_name} has been successfully copied')
    else:
        print(f'File {file_name} was not copied')


code = {
    '1': make_dir,
    '2': remove_dir,
    '3': list_dir,
    '4': copy_file
}
try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if code.get(key):
        code[key]()
    else:
        print('Key is incorrect')
        print('Type \'0\' for help')
