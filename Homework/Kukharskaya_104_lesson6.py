import random
# exersice_4
counter_1, counter_2 = int(input('Введите число от: ')), int(input('Введите число до: '))

while counter_1 < -1:  # задаём циклу условие, чтобы числа были отрицательные
    counter_1 += 1  # переход на новую итерацию
    print(counter_1)  # выводим результат

# exersice_6
digit_1, digit_2 = float(input('Введите число для операции: ')), float(input('Введите число для операции: '))
symbol = input('Введите + - * /: ')
while True:  # вводим цикл - истинно
    if symbol == '0':  # завершает операцию, если введён, как символ
        break
    elif symbol == '+':  # если введённый символ +
        print(f'{digit_1} + {digit_2} = {digit_1 + digit_2}')  # выводим операцию сложения
    elif symbol == '-':  # если введённый символ -
        print(f'{digit_1} - {digit_2} = {digit_1 - digit_2}')  # выводим операцию вычитания
    elif symbol == '*':  # если введённый символ *
        print(f'{digit_1} * {digit_2} = {digit_1 * digit_2}')  # выводим операцию умножения
    elif symbol == '/':  # если символ /
        if digit_2 != 0:  # если второе введённое число != 0
            print(f'{digit_1} / {digit_2} = {digit_1 / digit_2}')  # выводим операцию деления
        else:  # иначе (второе число == 0)
            print('Деление на ноль!')  # выводит
    break  # прерывает цикл

# exersice_7
arr = [1, 4, 6, 9, 2, 1, 5]  # задаём список из 7 элементов

arr_even = []  # пустой список для четных чисел
arr_uneven = []  # пустой список для нечетных чисел
total = arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6]  # сумма всех чисел списка

for num_ in arr:  # задаём цикл
    if num_ % 2 == 0:  # находим чётные числа в списке
        arr_even.append(num_)  # добавляем только чётные числа в список
    else:  # иначе
        arr_uneven.append(num_)  # добавляем нечётные числа в список
if len(arr_even) > len(arr_uneven):  # сравниваем, если больше четных
    print(total)  # выводим сумму
else:
    print(arr[0] * arr[2] * arr[5])  # если больше нечетных, то произведение 1, 3, 6 элементов списка


# homework

dig_1 = random.randint(1, 10)
dig_color_ = random.randint(1, 2)  # 1 - черный, 2 - красный

count_ = 1  # счётчик
while count_ <= 5:  # вводим цикл >= 5, тк 5 попыток у пользователя
    effort_, effort_color_ = int(input('Введите число от 1 до 10: ')), int(input('Введите число 1 или 2: '))
    # пользователь вводит данные
    if effort_ == dig_1 and effort_color_ == dig_color_:  # сравниваем введённые данные с рандом
        print('You are a winner!!!')  # если равны, то выводим, что пользователь выиграл
        break  # соответственно прерываем цикл
    else:  # если нет, то пользователь использует оставшиеся попытки
        print('Try again...')

    if count_ == 5:  # после 5 попытки
        print(f'Right combination: {dig_1} and {dig_color_}!')  # выводит правильную комбинацию для пользователя

    count_ += 1  # запускает след итерацию
