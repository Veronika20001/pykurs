# Убирает символ из строки, введённый пользователем
string_ = input('Введите строку: ')
symbol = input('Введите символ: ')
new_string = ""

for i in string_:
    if i != symbol:
        new_string += i
print(new_string)

# exersice_2
start_ = int(input('Введите начало последовательности: '))
stop_ = int(input('Введите конец последовательности: '))
step_ = int(input('Введите шаг'))
for _ in range(start_, stop_, step_):
    print(_)

# exersice_3
# выводит число от 54 до 9184, кратное 5
for i in range(54, 9184):
    if i % 5 == 0:
        print(i)

arr = ['рыба', 'курица', 'говядина']
for i in arr:
    if i == 'рыба':
        print(f'Я не ем {i}')
    break

from array import *

arr = array('i', [1, 4, 6, 7])
dig = ['string', 1.2, 4]
print(type(arr))
print(type(dig))

# создание массива
arr_ = []
for i in range(1, 11):
    arr_ += [i]
print(arr_)