# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class ToyAnimal(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'Animal'


class ToyCartoon(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'Cartoon'


class ToyToxic(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'ToxicToy'


class ToyManufacture:
    def create_toy(self, name, color, toy_type):
        self._purchase_raw_materials()
        self._sewing()
        self._set_color()
        if toy_type == 'Animal':
            return ToyAnimal(name, color)
        elif toy_type == 'Cartoon':
            return ToyCartoon(name, color)
        else:
            return ToyToxic(name, color)

    def _purchase_raw_materials(self):
        print('Buying the materials')

    def _sewing(self):
        print('Sewing toys')

    def _set_color(self):
        print('Painting the toys')


if __name__ == '__main__':
    toy_factory = ToyManufacture()
    toy = toy_factory.create_toy('Bim', 'Black_White', 'Animal')
    print(isinstance(toy, ToyCartoon))
    print(isinstance(toy, ToyAnimal))
    print(isinstance(toy, Toy))

    if isinstance(toy, ToyToxic):
        print('Toxic toy is danger for kids')
    else:
        print('Toy is safety for kids')
