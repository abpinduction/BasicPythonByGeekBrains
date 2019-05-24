# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random


class Person:

    def __init__(self, name, health=100, armor=2):
        self._name = name
        self._health = health
        self._armor = random.randint(2, 20)
        self._damage = random.randint(20, 500)
        self._lvl = 1

    def get_name(self):
        return self._name

    def get_health(self):
        return self._health

    def get_damage(self):
        return self._damage

    def get_armor(self):
        return self._armor

    def _set_health(self, value):
        self._health = value

    # method of getting damage for player
    def hit(self, damage):
        self._set_health(self._health - damage)

    def _real_damage(self, enemy):
        return self._damage / enemy.get_armor()

    def attack(self, enemy):
        damage = self._real_damage(enemy)
        enemy.hit(damage)


class Player(Person):

    def __init__(self, name, health):
        super().__init__(name, health)
        self._experience = 1
        self._exp_to_next_lvl = 100

    def get_exp(self):
        return self._experience

    def _is_next_lvl(self):
        if self._experience >= self._exp_to_next_lvl:
            self._lvl += 1
            self._exp_to_next_lvl *= 2

    def increase_lvl(self, value):
        if value > 0:
            self._experience += value
            self._is_next_lvl()


class Enemy(Person):

    def __init__(self, name, lvl):
        super().__init__(name)
        self._lvl = lvl
        self._damage *= lvl
        self._armor *= lvl
        self._health *= lvl


class Game:
    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy

    def start(self):
        last_assaulter = self._player
        while self._player.get_health() > 0 and self._enemy.get_health() > 0:
            if last_assaulter == self._player:
                self._enemy.attack(self._player)
                last_assaulter = self._enemy
            else:
                self._player.attack(self._enemy)
                last_assaulter = self._player
        if self._player.get_health() > 0:
            print(f'{self._player.get_name()} has won')
        else:
            print(f'{self._enemy.get_name()} has won')


if __name__ == "__main__":
    hero = Player('Batman', 5000)
    bad_hero = Enemy('Joker', 2)
    game = Game(hero, bad_hero)
    game.start()
