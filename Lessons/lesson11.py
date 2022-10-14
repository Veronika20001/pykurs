import random

s = ['pythonist'.count(x) for x in 'pythonist']
print(s)

s1 = {x: 'pythonist'.count(x) for x in 'pythonist'}
print(s1)

a = [random.randint(1, 10) for x in range(10)]
print(a)

o = {'a': 10, 'b': 10}
n = {}
for i, j in o.items():
    n[j] = i
print(n)


def factorial(n):
    if n != 0:
        return n * factorial(n - 1)
    else:
        return 1


print(factorial(5))


def sum_(a, b):
    return a + b


s = sum_(1, 2)
x = sum_  # ссылаемся на название функции
print(s, x(1, 2))


def func(x): return x


a1 = func
a2 = a1

print(a2(10))


# exercise_1
def func_(dig):
    count = 0
    while dig > 0:
        dig = dig // 10
        count += 1
    return count


print(func_(int(input('Введите число: '))))


# exercise_2
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


# example
def many(*args, **kwargs):
    print(args, kwargs)  # (1, 2, 3) {'name': 'mike', 'job': 'program'}


many(1, 2, 3, name='mike', job='program')


# example_2
def sum_(a, b):
    return a + b


s = sum_(1, 2)
x = sum_  # ссылается на нашу функцию
print(s, x(2, 5))


# example (присвоение функции переменной) - непрямой вызов функции
def func(x): return x


a1 = func
a2 = a1

print(a2(10))

# вызов функции в функции
def mul(a):
    def helper(b):
        return a * b

    return helper


print(mul(3)(2))  # a i b


# наработка!!!!!
# '''Написать функцию и сделать так, чтобы число секунд
# отображалось в виде дни:часы:минуты:секунды.'''
#
#
# def sec_(seconds):
#     def min_(minutes):
#         minutes = seconds / 60
#
#         def hours_(hour):
#             hour = minutes / 60
#
#         return hours_()
#
#     return min_()
#     # print(f'{hour}: {minutes}: {seconds}')
#
#
# sec_(120)
