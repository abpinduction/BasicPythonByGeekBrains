# ADVANCE
# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

first_name = input('Name: ')
last_name = input('Surname: ')
age = int(input('Age: '))
weight = int(input('Weight: '))

if weight < 50 or weight > 120:
    if 30 < age < 40:
        print(first_name, ', ', last_name, ', ', age, ' years old , ', 'weight ',
              weight, 'kg - keep healthy life style')
    elif 40 <= age < 70:
        print(first_name, ', ', last_name, ', ', age, ' years old, ', 'weight ', weight, 'kg - visit your doctor!')
    elif 70 <= age <= 170:
        print(first_name, ', ', last_name, ', ', age, ' years old, ', 'weight ', weight,
              ' - get your ducks in a row -)')
    elif age > 170:
        print('AGE IS INCORRECT')
    else:
        print('this test for adult only')
else:
    if 18 < age <= 30:
        print(first_name, ', ', last_name, ', ', age, ' years old, ', 'weight ', weight, 'kg - you are good')
    elif 30 < age < 70:
        print(first_name, ', ', last_name, ', ', age, ' years old, ', 'weight ',
        weight, 'kg - keep healthy life style')
    elif 70 <= age <= 170:
        print(first_name, ', ', last_name, ', ', age, ' years old, ', 'weight ', weight, 'kg - you are the best one!')
    elif age > 170:
        print('AGE IS INCORRECT')
    else:
        print('this test for adult only')
