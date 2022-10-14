# задание_1
num_1, num_2, num_3 = int(input()), int(input()), int(input())

print(num_1 + num_2, num_2 ** num_1, num_3 - num_2, num_1 / num_2)

# задание_2
num1 = 17 / 2 * 3 + 2
num2 = 2 + 17 / 2 * 3
num3 = 19 % 4 + 15 / 2 * 3
num4 = (15 + 6) - 10 * 4
num5 = 17 / 2 % 2 * 3 ** 3
print(num1, num2, num3, num4, num5)  # вывод полученного результата вычислений

# задание_3
rub = 11
bread = 1.5

print(rub - (3 * bread))

# задание_4
age = ((30 + 33 + 24 + 28 + 31 + 33 + 38 + 29 + 22 + 31 + 28 + 15 + 32 + 29 + 21 + 41 + 49) / 17)
print(age)

# задание_5
from math import *

degrees = float(input())
rad = radians(degrees)

print(rad)

# задание_6
from math import *

a, b, c = float(input()), float(input()), float(input())
discriminant = pow(b, 2) - 4 * a * c
print(discriminant)

# задание_7
import random

num = random.randint(100, 999)
num1 = num // 100
num2 = (num % 100) // 10
num3 = num % 10
print(num1 + num2 + num3)

# задания_8
a = float(input('Введите катет: '))
b = float(input('Введите катет: '))
c = float(input('Введите гипотенузу: '))
print('Периметр =', a + b + c)
print('Площадь =', (a * b) / 2)
