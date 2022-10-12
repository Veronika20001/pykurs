# exercise_3
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

print(d1['b'] == d2['b'])

# exercise_4
dict_ = {'dig_1': 11, 'dig_2': 25, 'dig_3': 37, 'dig_4': 10}
count = 1
for key in dict_:
    count = count * dict_[key]
print(count)

# exercise_5
list_1 = ['one', 'two', 'three', 'four']
list_2 = [1, 2, 3, 4]
dict_ = dict(zip(list_1, list_2))
print(dict_)

# exercise_6
word = 'pythonist'
dict_ = {x: word.count(x) for x in word}
print(dict_)

'''
У вас есть словарь, где ключ - название продукта.
Значение - список, который содержит цену и количество товара.
Выведите через "-" название - цену - количество.
С клавиатуры вводите название товара и его количество.
n - выход их программы.
Посчитайте цену выбранных товаров и сколько товаров осталось в изначальном списке
'''

product_ = {'bread': [3.5, 6],
            'oil': [4.1, 10],
            'icecream': [1.9, 12]}
for key, value in product_.items():  # цикл, чтобы вывести ключ-значение словаря
    print(f'{key} - {value[0]} - {value[1]}')


# homework
def product():  # объявляем функцию
    while True:  # запускаем цикл
        user_product = input('Введите название продукта: ')
        if user_product in product_:  # если введённый продукт есть в нашем словаре, выполняются след блоки
            if product_[user_product][1] == 0:  # если товар закончился
                print('К сожалению, товар закончился!')
                exit2 = input('Введите n для выхода: ')
                if exit2 == 'n':  # для выхода
                    break
            elif product_[user_product][1] > 0:  # если товар есть
                user_amount = int(input('Введите количество продукта: '))
                product_[user_product][1] = product_[user_product][1] - user_amount
                print(f'Стоимость: {product_[user_product][0] * user_amount}')
                print(f'Осталось товара: {product_[user_product][1]}')
                for i, x in product_.items():
                    print(f'{i} - {x[0]} - {x[1]}')
                exit1 = input('Введите n для выхода: ')
                if exit1 == 'n':
                    break
            else:  # если ввели товар больше, чем есть в наличии
                print('Неверное количество товара!')
                exit3 = input('Введите n для выхода: ')
                if exit3 == 'n':
                    break
        else:  # если нет товара, который ввели
            print('Данного товара нет!')
            exit4 = input('Введите n для выхода: ')
            if exit4 == 'n':
                break
    for i, x in product_.items():  # запускаем цикл, где выведутся остатки
        print(f'Итого осталось: {i} - {x[0]} - {x[1]}')
    return product_


product()  # вызываем функцию
