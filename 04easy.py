# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

rand_lst = [2, 4, 6, 8, 3, 7, 9]
pow_lst = [i * i for i in rand_lst]
print(pow_lst)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

european_fruits = ['apple', 'pear', 'plum', 'orange', 'cherry', 'banana']
exotic_fruits = ['kiwi', 'orange', 'banana', 'guava', 'mango', 'pineapple']
common_fruits = [fruit for fruit in european_fruits if fruit in exotic_fruits]
print(common_fruits)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

random_num = [3, 5, 144, -5464, 21, -252351, 626, 213, 78, 224, 16]
my_lst = [num for num in random_num if num % 3 == 0 and num > 0 and num % 4 != 0]
print(my_lst)
