# Задание:
# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!

person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    """
    расширим возможность введения пин кода до трех попыток
    """
    chance = 3
    while person['pin'] != pin_code:
        print(f'Будьте внимательны. Осталось {chance} попытки')
        chance -= 1
        if chance < 0:
            break
        try:
            pin_code = int(input('Введите пин код: '))
        except ValueError:
            print('Пин код - 4 цифры без букв и спец символов!')
    return True


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    # прверка на ввод отрицательной суммы
    if money < 0:
        return 'Неправильно набрана сумма'
    # if person['money'] - money == 0: - ошибка логики - если у человека нет денег на карте
    # он не может снять денег и уйти в минусовой баланс
    if person['money'] - money > 0:
        person['money'] -= money
        return f'Вы сняли {money} рублей.'
    else:
        return 'На вашем счету недостаточно средств!'


def process_user_choice(choice, person):
    # проверка на ввод неправильных цифр.
    while choice > 3 or choice < 1:
        choice = int(input('Введите номер операции согласно списка меню: '))
    if choice == 1:
        print(f'На Вашем счету: {check_account(person)}')
    if choice == 2:
        try:
            take_money = float(input('Сумма к снятию: '))
            print(withdraw_money(person, take_money))
        except ValueError:
            print('Неправильно набрана сумма')


def start():
    card_number, pin_code = input('Введите номер карты и пин код через пробел: ').split()
    # Проверка на ввод букв вместо цифр
    try:
        pin_code = int(pin_code)
    except ValueError:
        print('Пин код не верен!')
    try:
        card_number = int(card_number)
    except ValueError:
        print('Номер карты не верен!')
    person = get_person_by_card(card_number)
    if person and is_pin_valid(person, pin_code):
        while True:
            try:
                choice = int(input('Выберите пункт:\n'
                                   '1. Проверить баланс\n'
                                   '2. Снять деньги\n'
                                   '3. Выход\n'
                                   '---------------------\n'
                                   'Ваш выбор: '))
                if choice == 3:
                    print('HOPE TO SEE YOU SOON!\n'
                          'GOOD BUY, SIR!')
                    break
                process_user_choice(choice, person)
            except ValueError:
                print('Введите номер операции согласно списка меню: ')
    else:
        print('Номер карты или пин код введены не верно!')


start()
