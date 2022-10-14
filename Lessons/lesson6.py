n = 0
while n < 5:  # 0 < 5 == True
    n += 1
    print(n)
    print('итерация')

# exersice_1
i = 0
while i <= 10:
    i += 1
    print(i ** 2)

# exersice_2
i = 0
result = 1
while i <= 125:  # задаём циклу условие от 0 до 125
    i += 1  # переход на новую итерацию
    if i % 2 == 0:  # остаток от деления на 2, выводим только четные числа
        result *= i  # умножаем только чётные числа полученные при итерации
print(result)  # выводим результат умноженных чёт чисел


# вывести по убыванию числа
counter = 15
while counter > 0:  # 15 > 0
    print(counter * ' ', counter)
    counter -= 1

# вывести по убыванию числа
list_ = list(range(1, 16))
list_.reverse()
print(*list_)


i = 7
list_ = []
while i < 100:
    list_.append(i)
    i += 7
print(f'Список: {list_}, Длина строки: {len(list_)}')