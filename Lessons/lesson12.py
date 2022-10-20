# f = open('example.txt', 'r')  # открыть файл из рабочей директории в режиме чтения (относительный путь)
# fp = open('C:/xyz.txt', 'r')  # (абсолютный путь) открыть файл из любого каталога
# print(*f)
# print(f)


try:
    k = 1 / 0
except ZeroDivisionError:
    k = 0

print(k)

# example_1

my_dict = {'a': 1, 'b': 2, 'c': 3}

try:
    value = my_dict['d']
except KeyError:
    print('Ключа не существует!')

# example_2

my_list = [1, 2, 3, 4, 5]

try:
    my_list[6]
except IndexError:
    print('Этого индекса нет в списке!')

# example_3

my_dict = {'a': 1, 'b': 2, 'c': 3}

try:
    value = my_dict['d']
except IndexError:
    print('Такого индекса не существует!')
except KeyError:
    print('Ключа не существует!')
except:
    print('Произошла другая ошибка')


# example_4

my_dict = {'a': 1, 'b': 2, 'c': 3}

try:
    value = my_dict['d']
except (IndexError, KeyError):
    print('Произошла ошибка!')


# example_5

my_dict = {'a': 1, 'b': 2, 'c': 3}

try:
    value = my_dict['d']
except KeyError:
    print('Произошла ошибка KeyError!')
else:
    print('Ошибок не произошло!')
finally:  # выполняет блок инструкций в любом случае, было ли искл или нет
    print('Оператор finally выполнен!')
# применяется, когда нужно непременно что-то сделать, к примеру закрыть файл


# exercise_3
def summ_(a, b):
    res = a + b
    print(res)


def minus_(a, b):
    res = a - b
    print(res)


def multi_(a, b):
    res = a * b
    print(res)


def division(a, b):
    try:
        res = a / b
        print(res)
    except ZeroDivisionError:
        print('Произошло деление на 0!')
    finally:
        print('Операция выполнена!')


def calculator_(a, b):
    symbol = input('Введите + - * /: ')
    if symbol == '+':
        summ_(a, b)
    elif symbol == '-':
        minus_(a, b)
    elif symbol == '*':
        multi_(a, b)
    elif symbol == '/':
        division(a, b)


a1, b1 = float(input('Введите число для операции: ')), float(input('Введите число для операции: '))

calculator_(a1, b1)