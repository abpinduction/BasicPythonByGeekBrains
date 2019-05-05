# coding=utf-8
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   pwd - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

import os
import shutil
import sys

print('sys.argv = ', sys.argv)


def print_help():
    print('help - получение справки')
    print('mkdir <dir_name> - создание директории')
    print('ping - тестовый ключ')
    print('cp <file_name> - создает копию указанного файла')
    print('rm <file_name> - удаляет указанный файл')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('pwd - отображение полного пути текущей директории')


def mkdir():
    if not parameter:
        print('Необходимо указать имя директории вторым параметром')
        return False
    dir_path = os.path.join(os.getcwd(), parameter)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(parameter))
    except FileExistsError:
        print('директория {} уже существует'.format(parameter))


def ping():
    print("pong")


def cp():
    if not parameter:
        print('Необходимо указать имя файла вторым параметром')
        return False
    if os.path.isfile(parameter):  # проверка есть ли такой файл
        copyfile = 'copy_of.' + parameter
        shutil.copy(parameter, copyfile)
        if os.path.exists(copyfile):  # существует ли копия файла
            print('Файл {} скопирован'.format(parameter))
            return True
        else:
            print('Возникли проблемы копирования')
            return False
    else:
        print('Файл {} не найден'.format(parameter))


# более компактный вариант функции cp()
# def cp(filename):
#     with open(filename, 'rb') as f:
#         with open('copy_' + filename, 'wb') as destination_f:
#             destination_f.write(f.read())


def rm():
    if not parameter:
        print('Необходимо указать имя файла вторым параметром')
        return
    if os.path.isfile(parameter):  # проверка есть ли такое имя файла
        answer = input('Вы уверены? Y/N: ')
        if answer == 'Y':
            os.remove(parameter)
        else:
            print('Файл {} не удален'.format(parameter))
            return
        if os.path.exists(parameter):
            print('Файл {} не удален'.format(parameter))
        else:
            print(f'Файл {parameter} удален')
    else:
        print('Файл {} не найден'.format(parameter))


# более компактный вариант функции rm()
# def rm(filename):
#     result = input('Вы уверены? y/n:')
#     if result == 'y':
#         try:
#             os.remove(filename)
#         except FileNotFoundError:
#             print('Файл для удаления не найден.')


def cd():
    if not parameter:
        print('Необходимо указать новый путь вторым параметром')
        return
    try:
        os.chdir(parameter)
    except FileNotFoundError:
        print('Директория не найдена')


def pwd():
    try:
        print(os.getcwd())
    except FileNotFoundError:
        print('Директория не найдена')


do = {
    "help": print_help,
    "mkdir": mkdir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "pwd": pwd
}

try:
    parameter = sys.argv[2]
except IndexError:
    parameter = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print('Задан неверный ключ\nУкажите ключ help для получения справки')
