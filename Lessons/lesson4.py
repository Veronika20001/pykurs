# ex_1
num_1 = int(input('Введите целое число: '))

if num_1 % 2 == 0:
    print(f'Число {num_1} является чётным')
else:
    print(f'Число {num_1} - нечётное')

# ex_2
fing = int(input('Введите порядковый номер пальца руки: '))
if fing == 1:
    print('большой')
elif fing == 2:
    print('указательный')
elif fing == 3:
    print('средний')
elif fing == 4:
    print('безымянный')
elif fing == 5:
    print('мизинец')
else:
    print('такого пальца нет')

# ex_3
month = int(input('Введите месяц: '))
if 1 < month < 12:
    if month == 12 or month == 1 or month == 2:
        print('зима')
    elif month == 3 or month == 4 or month == 5:
        print('весна')
    elif month == 6 or month == 7 or month == 8:
        print('лето')
    elif month == 9 or month == 10 or month == 11:
        print('осень')
else:
    print('Нет такого месяца')

# ex_4
num_1, num_2, num_3 = int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: '))
if num_1 > num_2 and num_1 > num_3:
    print(num_1)
elif num_2 > num_1 and num_2 > num_3:
    print(num_2)
elif num_3 > num_1 and num_3 > num_1:
    print(num_3)
else:
    print('числа равны')

# ex_5
import random

num_1 = random.randint(1, 3)
if num_1 == 1:
    print('Камень')
elif num_1 == 2:
    print('Ножницы')
else:
    print('Бумага')

# ex_6
num_1, num_2 = int(input()), int(input())

compare = num_1 > num_2

if compare:
    print('True')
else:
    print('False')

# ex_7
num1, num2 = float(input('Введите число: ')), float(input('Введите число: '))
sign = input('Знак операции: ')
if sign == '+':
    print(num1 + num2)
elif sign == '-':
    print(num1 - num2)
elif sign == '*':
    print(num1 * num2)
elif sign == '/':
    if num2 == 0:
        print('На ноль делить нельзя')
    else:
        print(num1 / num2)
else:
    print('Ошибка')

# ex_8
string_ = input('Введите строку: ')  # считывает введённую пользователем строку

is_mister = (string_ == 'Mister')  # используем предикат, который проверяет является ли введённая строка = Mister
print(is_mister)  # выводит True / False
