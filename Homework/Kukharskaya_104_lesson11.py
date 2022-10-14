from random import *

# exercise_1
'''Написать функцию, которая определяет количество разрядов
введенного целого числа'''


def ranks(dig_):  # функция, вычисляющая разряды
    count = 0  # счётчик
    while dig_ > 0:  # цикл, если число больше 0
        dig_ //= 10  # целочисленное деление на 10
        count += 1  # к счётчику добавляется +1
    return count  # возвращаем наш счетчик после отработки цикла


print(ranks(int(input('Введите число: '))))  # вызываем функцию, где передаем аргумент, вводимый с клавиатуры

# exercise_2
'''В зависимости от выбора пользователя вычислить площадь
круга, прямоугольника или треугольника. Для вычисления
площади каждой фигуры должна быть написана отдельная
функция'''


def square_circle(r):
    return 3.14 * (r ** 2)


def square_triangle(a, h):
    return 0.5 * a * h


def square_rectangle(a, b):
    return a * b


def square_():
    user_choice = input('Введите, площадь чего хотите вычислить (треугольник, круг, прямоугольник): ')
    if user_choice == 'треугольник':
        print(square_triangle(int(input('Введите длину основания: '), int(input('Введите высоту')))))
    elif user_choice == 'круг':
        print(square_circle(int(input('Введите радиус: '))))
    elif user_choice == 'прямоугольник':
        print(square_rectangle(int(input('Введите длину высоты: '), int(input('Введите длину ширины')))))
    else:
        print('Введено неверно')


square_()

# exercise_3
'''Написать функцию, которая заполняет массив длинной 10
элементов, случайными числами в диапазоне, указанном
пользователем с клавиатуры. Функция должна принимать два
аргумента – начало диапазона и его конец, при этом ничего не
возвращать.'''


def arr_(start_, end_):
    array_ = [randint(start_, end_) for x in range(10)]
    return array_


start = int(input('Введите число: '))
end = int(input('Введите число: '))

print(arr_(start, end))

# exercise_4
'''Написать функцию и сделать так, чтобы число секунд
отображалось в виде дни:часы:минуты:секунды.'''


def sec_(seconds):
    minutes = seconds / 60
    hour = minutes / 60
    day = hour / 24
    print(f'{int(day)}: {int(hour)}: {int(minutes)}: {int(seconds)}')


sec_(int(input('Введите число секунд: ')))

# exercise_5
'''Написать функцию, которая считает сколько гласных и согласных
в строке. Строку вводить с клавиатуры.'''


def letters(user_string):
    count_vowels = 0
    count_consonants = 0
    for i in user_string:
        if i in 'ауоиэыяюеё':
            count_vowels += 1
        else:
            count_consonants += 1
    print(f'Гласные: {count_vowels}')
    print(f'Согласные: {count_consonants}')


letters(input('Введите строку на русском языке: '))
