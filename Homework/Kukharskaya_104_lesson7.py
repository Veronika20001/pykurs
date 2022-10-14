from math import *
from random import *


# exercise_2
def is_year_leap(year):  # определяем функцию
    if year % 4 == 0 or year % 400 == 0 and year % 100 == 0:  # задаём условие
        return True  # при его выполнении возвращаем True
    else:
        return False  # при его не выполнении возвращаем False


print(is_year_leap(int(input('Введите год, чтобы узнать високосный ли он: '))))  # вызываем функцию


# exersice_3
def square(side):  # определяем функцию
    perimeter = 4 * side  # задаём переменные с операциями
    sqr_ = pow(side, 2)
    diagonal = side * sqrt(2)

    return perimeter, sqr_, diagonal  # возвращаем значения


print(square(int(input('Введите сторону квадрата: '))))  # вызываем функцию и выводим


# exersice_4
def season(month):  # определяем функцию и задаём условия
    if 1 < month < 12:
        if month == 12 or month == 1 or month == 2:
            print('зима')
        elif month == 3 or month == 4 or month == 5:
            print('весна')
        elif month == 6 or month == 7 or month == 8:
            print('лето')
        elif month == 9 or month == 10 or month == 11:
            print('осень')
    else:  # при не исполнении первого блока переходит к else
        print('Нет такого месяца')


month_ = int(input('Введите месяц 1-12: '))  # пользователь вводит данные типа integer
season(month_)  # вызываем функцию


# exersice_5 (не поняла как реализовать с простым числом)
def is_prime(n):  # определяем функцию
    d = 2
    while n % d != 0:
        d += 1
    return d == n


n = randint(0, 1000)
print(n)
print(is_prime(n))  # вызываем функцию и выводим

# exersice_6
new_arr = []  # пустой список

for i in range(10):  # запускаем цикл, тк необходимо 10 чисел в списке
    new_arr.append(randint(1, 250))  # добавляем в список случайные числа от 1 до 250
print(new_arr)  # выводим новый список


def average_(new_arr):  # определяем функцию
    return sum(new_arr) / len(new_arr)  # возвращаем значение сумма элементов списка / на кол-во элементов в нём


print(average_(new_arr))  # вызываем функцию и выводим


# homework
def calculator_():  # определяем функцию
    digit_1, digit_2 = float(input('Введите число для операции: ')), float(input('Введите число для операции: '))
    symbol = input('Введите + - * /: ')
    if symbol == '+':  # если введённый символ +
        print(f'{digit_1} + {digit_2} = {digit_1 + digit_2}')  # выводим операцию сложения
    elif symbol == '-':  # если введённый символ -
        print(f'{digit_1} - {digit_2} = {digit_1 - digit_2}')  # выводим операцию вычитания
    elif symbol == '*':  # если введённый символ *
        print(f'{digit_1} * {digit_2} = {digit_1 * digit_2}')  # выводим операцию умножения
    elif symbol == '/':  # если символ /
        if digit_2 != 0:  # если второе введённое число != 0
            print(f'{digit_1} / {digit_2} = {digit_1 / digit_2}')  # выводим операцию деления
        else:  # иначе (второе число == 0)
            print('Деление на ноль!')  # выводит


calculator_()  # вызываем функцию

# калькулятор через функции
digit_1, digit_2 = float(input('Введите число для операции: ')), float(input('Введите число для операции: '))
symbol = input('Введите + - * /: ')
if symbol == '+':
    def plus_(digit_1, digit_2):
        return digit_1 + digit_2


    print(plus_(digit_1, digit_2))

elif symbol == '-':
    def minus_(digit_1, digit_2):
        return digit_1 - digit_2


    print(minus_(digit_1, digit_2))
elif symbol == '*':

    def multi_(digit_1, digit_2):
        return digit_1 * digit_2


    print(multi_(digit_1, digit_2))
elif symbol == '/':

    def division_(digit_1, digit_2):
        if digit_2 != 0:
            return digit_1 / digit_2
        else:
            return 'Деление на ноль!'


    print(division_(digit_1, digit_2))