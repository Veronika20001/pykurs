'1. Напишите рекурсивную функцию получения факториала числа n'


def factorial(n):
    if n != 0:
        return n * factorial(n - 1)
    else:
        return 1


print(factorial(7))

'2. Напишите функцию, которая будет возвращать последовательность фибоначчи в заданном диапазоне от 0 до n'


# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(11))

def fibonacci(n):
    num_1 = 1
    num_2 = 1
    for i in range(n):
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


print(list(fibonacci(11)))

'Дано 2 словаря, создать третий словарь, чтобы он отсортировывал по длине ключей из словарей'

dict_1 = {'верный': [11, 55.2, 'слон'], 'фиолетовый': 15, 'орда': 'восемь'}
dict_2 = {'ода': {52, 99, 2}, 'сороконожка': {110, 'слово', 15}}

dict_ = dict_1 | dict_2
# print(dict_)

dict_3 = {}
for key in sorted(dict_, key=len, reverse=False):
    dict_3[key] = dict_[key]

print(dict_3)

'''Дана строка "Что это было?... Я не ожидал увидеть подобного, но мне придётся принять решение"
Вывести:
1. Строку без знаков препинания
2. Строку без букв верхнего регистра
3. Всю строку в верхнем регистре
4. Строку, изменив регистр букв(наоборот)
5. Строку, заменив все знаки препинания на пробел'''

string = 'Что это было ?...Я не ожидал увидеть подобного, но мне придётся принять решение'


string_ = string[:]
alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '

for i in string_.lower():
    if i not in alpha:
        string_ = string_.replace(i, '')
print(string_)  # 1. Строку без знаков препинания
print(string.lower())  # 2. Строку без букв верхнего  регистра
print(string.upper())  # 3. Всю строку в верхнем регистре
print(string.swapcase())  # 4. Строку, изменив регистр букв (с нижнего на верхний и наоборот)
for i in string.lower():
    if i not in alpha:
        string_1 = string_.replace(i, ' ')
print(string_1)  # 5. Строку, заменив все знаки препинания на пробел
