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


def func_(dig):
    count = 0
    while dig > 0:
        dig = dig // 10
        count += 1
    return count


print(func_(int(input('Введите число: '))))
