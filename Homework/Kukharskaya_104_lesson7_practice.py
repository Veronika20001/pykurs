from math import *
from random import *

# задание_1
''' Вычислить длину гипотенузы по двум введённым катетам'''


def length_():  # объявляем функцию
    side_1 = float(input('Введите катет 1: '))  # запрашивает у пользователя ввести число
    side_2 = float(input('Введите катет 2: '))  # запрашивает у пользователя ввести число
    return sqrt(pow(side_1, 2) + pow(side_2, 2))  # возвращает значение формулы вычисления гипотенузы


print(length_())  # вызываем функцию и выводим

# задание_2
'''Вводится 3 числа, найти среднее (больше одного, меньше другого)'''
print('Введите 3 разных числа.')


def average_():
    dig_1 = float(input('Введите число: '))
    dig_2 = float(input('Введите число: '))
    dig_3 = float(input('Введите число: '))
    if dig_1 < dig_2 < dig_3 or dig_3 < dig_2 < dig_1:
        return dig_2
    elif dig_2 < dig_1 < dig_3 or dig_3 < dig_1 < dig_2:
        return dig_1
    elif dig_1 < dig_3 < dig_2 or dig_2 < dig_3 < dig_1:
        return dig_3


print(average_())

# задание_3
'''Два случайных числа. Одно - четное, другое - нечётное, Определить и вывести нечётное число'''


def digit_():
    dig_1, dig_2 = randrange(2, 100, 2), randrange(1, 100, 2)
    if dig_1 % 2 != 0 and dig_2 % 2 == 0:
        return dig_1
    elif dig_2 % 2 != 0 and dig_1 % 2 == 0:
        return dig_2


print(digit_())

# задание_4 (пока только так додумалась)
'''Вывести число наоборот'''


def reverse_(dig_):
    dig_1 = dig_ // 1000
    dig_2 = (dig_ // 100) % 10
    dig_3 = (dig_ // 10) % 10
    dig_4 = dig_ % 10
    print(dig_4, dig_3, dig_2, dig_1, end='')


reverse_(6547)


# задание_5
def draw_box(width):
    print('*' * width)
    for i in range(12):
        print('*', '_' * 6, '*')
    print('*' * width)


draw_box(10)

# задание_6

list_1 = []
sum_ = []
for i in range(2, 10000):
    for x in range(1, i):
        if i % x == 0:
            sum_.append(x)
    if sum(sum_) == i:
        list_1.append(i)
    sum_.clear()
print(list_1)

# задание_7

arr = []
for i in range(10):
    num = int(input("Введите число: "))
    if i < 9:
        arr.append(num)
    else:
        print(num)
num_1 = int(input("Введите ещё число: "))
index = int(input("Введите на какую позицию вставить число: "))
arr.insert(index - 1, num_1)
print(arr)


# задание_8
def word_(string_):
    print(len(string_.split()))


word_(input('Введите 4 слова через пробел:'))


# задание_9
def upper_clear(string_):
    new_str = ''
    for i in string_:
        if i.islower():
            new_str += i
    print(new_str)


upper_clear('FhjsssH')


# задание_10
def digit_7(dig_):
    for i in dig_:
        if i % 7 == 0:
            continue
        else:
            print(i)


digit_7(x for x in range(101))


# задание_11
def sum_(dig_1):
    print(sum(dig_1))


sum_(range(1, 101))


# задание_12
def factorial(num_):
    count = 1
    for i in range(1, num_ + 1):
        count *= i
    print(f'Факториал числа {num_}: {count}')


factorial(int(input('Введите число, факториал которого хотите узнать: ')))


# задание_13
def spruce(num_):
    count_ = 1
    step = 2
    for i in range(1, num_ + 1):
        print(i, end=' ')
        if i == count_:
            count_ += step
            print('\n')
            step += 1


spruce(int(input("Введите число: ")))


# задание_14
def power_two(num):
    tot = 1
    count = 1
    while tot < num:
        print(tot, end=" ")
        tot = 2 ** count
        count += 1


power_two(int(input('Введите число: ')))
