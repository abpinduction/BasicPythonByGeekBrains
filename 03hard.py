# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt

# Напишите функцию, которая будет:
# 1. считывать файл игрока
# 2. считывать файл его врага
# 3. получать оттуда данные, и
# 4. записывать их в словари
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

import random


def create_player():
    """
    для большего прикола игороки создаются с псевдослучайными значениями характеристик
    """
    player_name = input('Give a name to player: ')
    health = random.randint(300, 1000)
    damage = random.randint(10, 70)
    armor = random.uniform(1, 2)
    player = {'name': player_name, 'health': health, 'damage': damage, 'armor': armor}
    return player


def real_damage(damage, armor):
    return damage // armor


def fight(defender, assaulter, ):
    damage = real_damage(assaulter['damage'], defender['armor'])
    defender['health'] -= damage
    print(f'{assaulter["name"]} damaged the {defender["name"]} with injury {damage} and its health is '
          f'{defender["health"]} left')


def save_in_file(player):
    with open(player['name'] + '.txt', 'a', encoding='UTF-8') as file:
        for key, value in player.items():
            file.write(f'{key} {value}\n')
    return player['name'] + '.txt'


def get_from_file(filename):
    player = {}
    with open(filename, 'r', encoding='UTF-8') as dictionary:
        for line in dictionary:
            key, value = line.split()
            if key == 'armor':
                value = float(value)
            if key != 'name':
                value = int(value)
            player[key] = value
    return player


def game():
    player1 = create_player()
    player2 = create_player()
    save_in_file(player1)
    save_in_file(player2)

    while True:
        fight(player1, player2)
        if player2['health'] <= 0:
            print(f'{player1["name"]} has won!')
        elif player1['health'] <= 0:
            print(f'{player2["name"]} has won!')
            break
        fight(player2, player1)
        if player1['health'] <= 0:
            print(f'{player2["name"]} has won!')
        elif player2['health'] <= 0:
            print(f'{player1["name"]} has won!')
            break

    save_in_file(player1)
    save_in_file(player2)


game()
