# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из norm05_module.py
import os

import norm05_module


def menu():
    print('____AVAILABLE COMMANDS____')
    print('0 - menu description')
    print('1 - change directory')
    print('2 - content of current directory')
    print('3 - remove directory')
    print('4 - make directory')


def main():
    print("Hello!")
    name = input("What is your name?: ")
    print(name, ', Welcome to Smart_Editor!')
    answer = ''
    while answer != 'Q':
        print('Press \'Y\' for continue or \'Q\' for exit')
        answer = input()
        if answer == 'Y':
            menu()
            code = input('Input command number: ')
            if code == 0:
                menu()
            if code == '1':
                print(f'Current path: {os.defpath}')
                dir_path = input('Input path to change directory: ')
                print(norm05_module.ch_dir(dir_path))
            elif code == '2':
                norm05_module.list_dir()
            elif code == '3':
                dir_name = input('Input folder name to remove: ')
                norm05_module.remove_dir(dir_name)
            elif code == '4':
                dir_name = input('Input folder name to create: ')
                norm05_module.make_dir(dir_name)
        elif answer == 'Q':
            print("See you!")
        else:
            print("The answer is incorrect")


main()
