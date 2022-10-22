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


# homework
def error_(string_):
    digit = string_.split()
    if len(digit) == 2:
        try:
            dig_1 = int(digit[0])
            dig_2 = int(digit[1])
            print(dig_1 / dig_2)
        except ValueError:
            print('Введенная строка - не числа! ')
            error_(input('Введите 2 числа через пробел: '))
        except ZeroDivisionError:
            print('На ноль делить нельзя! ')
            error_(input('Введите 2 числа через пробел: '))
        except IndexError:
            print('Введено не 2 числа!')
        else:
            print('Без ошибок')


error_(input('Введите 2 числа через пробел: '))
