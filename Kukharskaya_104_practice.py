# exercise_1
def index_(growth, weight):
    bmi = weight / (growth * growth)
    print(bmi)
    if bmi < 16:
        print('Выраженный дефицит массы тела')
    elif 16 <= bmi < 18.50:
        print('Недостаточная масса тела')
    elif 18.50 <= bmi < 25:
        print('Норма')
    elif 25 <= bmi < 30:
        print('Избыточная масса тела')
    elif 30 <= bmi < 35:
        print('Ожирение первой степени')
    elif 35 <= bmi < 40:
        print('Ожирение второй степени')
    elif bmi >= 40:
        print('Ожирение третьей степени')


index_(float(input('Введите ваш рост в метрах: ')), float(input('Введите ваш вес в кг: ')))


# exercise_6
def list_(list_1):
    list_cl = []
    list_1.reverse()
    print(list_1)  # в перевернутом виде список
    print(list_1[2: 8])  # срез перевернутого списка от 2 до 7 эл-та
    list_1.pop(5)
    print(list_1)  # без 5 элемента

    duplicate = list(set(list_1))
    print(duplicate)  # без дубликата


list_([1, 23, 2, 'sun', 33, 1, 'morning', 5, 8, 9])


# exercise_2
def figure_(user_side):
    if user_side == 3:
        return 'Треугольник'
    elif user_side == 4:
        return 'Квадрат', 'Прямоугольник', 'Ромб'
    elif user_side == 5:
        return 'Пятиугольник'
    elif user_side == 6:
        return 'Шестиугольник'
    elif user_side == 7:
        return 'Семиугольник'
    elif user_side == 8:
        return 'Восьмиугольник'
    elif user_side == 9:
        return 'Пентагондодекаэдр'
    elif user_side == 10:
        return 'Десятигранник'
    else:
        return 'Неверное значение'


print(figure_(int(input('Введите число сторон от 3 до 10: '))))


# exercise_9
def anagramm_(word_1, word_2):
    list_1 = list(word_1)
    list_2 = list(word_2)

    list_1.sort()
    list_2.sort()
    position = 0
    matches = True
    while position < len(word_1) and matches:
        if list_1[position] == list_2[position]:
            position = position + 1
        else:
            matches = False
    return matches


print(anagramm_(input('Введите первое слово:'), input('Введите второе слово:')))


# exercise_4
def online_shop(user_amount):
    first_product = 10.95
    other_product = 2.95
    if user_amount == 1:
        return f'Общая сумма доставки: {first_product} $'
    elif user_amount > 1:
        return f'Общая сумма доставки: {first_product + (user_amount * other_product)} $'


print(online_shop(int(input('Введите количество товаров: '))))


# exercise_5
def fraction_(numerator, denominator):
    if numerator > denominator:
        frac = numerator
    else:
        frac = denominator
    while frac != 1:
        if numerator % frac == 0 and denominator % frac == 0:
            return numerator // frac, denominator // frac
        else:
            frac -= 1
    return numerator, denominator


print(fraction_(int(input('Введите числитель: ')), int(input('Введите знаменатель: '))))


# exercise_8
def sublist(_list_):
    count = 0
    for x in _list_:
        if type(x) == list:
            count += 1
    return count


print(sublist([1, 2, 3, [1, 5], [1, 6]]))


# exercise_3
def date_():
    month_ = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
              'ноябрь', 'декабрь']
    month_30_days = ['апрель', 'июнь', 'сентябрь', 'ноябрь']
    month_31_days = ['январь', 'март', 'май', 'июль', 'август', 'октябрь']
    new_month = ''
    if day == 31 and month == 'декабрь':
        print('1 января', year + 1)
    if month == 'февраль':
        if day == 28 and year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print('29 февраля', year)
        else:
            print('1 марта', year)
    if day == 30 and month in month_30_days or day == 31 and month in month_31_days:
        for index, value in enumerate(month_):
            if value == month:
                new_month = month_[index + 1]
        print('1', new_month, year)
    else:
        print(day + 1, month, year)


day = int(input('Введите день: '))
month = input('Введите месяц: ')
year = int(input('Введите год: '))

date_()


# exercise_7
def count_range(my_list, min_border, max_border):
    count = 0
    for i in my_list:
        if min_border <= i < max_border:
            count += 1
        return count


my_list_ = [1, 2, 3, 55, 64, 514, 20]
min_border_ = int(input('Введите минимальную границу: '))
max_border_ = int(input('Введите максимальную границу: '))
print(count_range(my_list_, min_border_, max_border_))


# exercise_10
def phone_(user_words):
    str_ = ''
    for i in user_words.upper():
        for key, value in dict_.items():
            if i in value:
                str_ += str(key) * (value.index(i) + 1)
    return str_


dict_ = {1: ".,?!:", 2: "ABC", 3: "DEF", 4: "GHI", 5: "JKL", 6: "MNO", 7: "PQRS", 8: "TUV", 9: "WXYZ", 0: " "}

words = input("Введите текст: ")
print(phone_(words))


# exercise_11
def flatten(data):
    list_ = []
    while data:
        iter = data.pop()
        if type(iter) == list:
            data.extend(iter)
        else:
            list_.append(iter)
    list_.sort()
    return list_


data_ = [1, [2, 3], [4, 5, 6], [7, [8, 9], 10]]
print(flatten(data_))
