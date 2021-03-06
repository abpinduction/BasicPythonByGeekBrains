# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

# Дан список, заполненный произвольными целыми числами
l1 = [2, -5, 8, 9, -25, 25, 4]
# получите новый список
l2 = []

for n in l1:
    # если результаты извлечения корня не имеют десятичной части и если такой корень вообще можно извлечь
    if math.sqrt(n).is_integer() and n > 0:
        # другой вариант n**0.5 == int(n**0.5) and n > 0:
        # элементами которого будут квадратные корни элементов исходного списка
        l2.append(math.sqrt(n))

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

# Дана дата в формате dd.mm.yyyy
date = input('Input date by format dd.mm.yyyy: ')

# создаем шаблоны текстового вывода дня
days = ('', 'первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',
        'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое',
        'восемнадцатое', 'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье',
        'двадцать чертвертое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое',
        'двадцать девятое', 'тридцатое', 'тридцать первое')
# создаем шаблоны текстового вывода месяца
months = ('', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
          'декабря')

day, month, year = date.split('.')
day = int(day)
month = int(month)
year = int(year)
# int(day) и int(month) - индексы списков days и months
print(days[day], months[month], year, 'года.')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

list1 = list()
n = int(input())
for _ in range(n):
    list1.append(random.randint(-100, 100))
print(list1)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]
# неповторяющиеся элементы исходного списка - set
exclude_duplicates = list(set(lst))
print(exclude_duplicates)

has_no_duplicates = list()
for i in lst:
    # элементы исходного списка, которые не имеют повторений - count(number) == 1
    if lst.count(i) == 1:
        has_no_duplicates.append(i)
print(has_no_duplicates)
