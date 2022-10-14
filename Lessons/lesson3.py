# задание_1
k = """abdg
ffjfk
ldjfn
jfjff 
"""
# тройные кавычки, для длинной информации
print(k)

# задание_2
name_ = input('Введите Ваше имя: ')
print('Привет, ' + name_)
print(name_ * 3)

# exc_2.1
user_name = input('Введите имя: ')
print(f"Привет, меня зовут {user_name}")
print(user_name * 3)

# задание_3
import random

num = str(random.randint(100, 999))
print(f"Сумма цифр трёхзначного числа {num} = ", int(num[0]) + int(num[1]) + int(num[2]))

# Конкатенация
s = 'string'
s1 = 1245
s2 = str(s1)
print(s + ' ' + s2)

# Класс Темплэйт
from string import Template

name = 'Vera'
age = 21

s = Template('Меня зовут $user. Мне $age лет.')
print(s.substitute(user=name, age=age))

# форматирование с помощью format()
name = 'Vera'
age = 21

s = 'Меня зовут {user}. Мне {age} лет.'.format(user=name, age=age)

print(s)

name = 'abc'
asd = 'der'
qwe = 'ghi'
print('{0:_<10}, {1:-^10}, {2:+>10}'.format(name, asd, qwe))
# exit abc_______, ---der----, +++++++ghi

# экранизация
string = 'i \\need \ a dollor'
print(string)

# задание на введение строки пользователем
s = input('Введите строку: ')  # запрашивает ввести строку у пользователя
print(s[::3])  # выводит каждый третий символ, включая 0 индекс
print(s[:1] + s[-1:])  # выводит первый и последний символ строки, без пробела
print(s.upper())  # выводит все символы строки в верхнем регистре
print(s[::-1])  # переворачивает и выводит строку
print(s.isdigit())  # является ли наша строка числом?

# задание на палиндром
s = input('Введите строку: ')  # запрашивает ввести строку у пользователя
s1 = s.replace(' ', '')  # метод убирает пробелы во введенной строке

print(s1[::-1] == s1)  # выводит является ли перевернутая строка = просто строке
