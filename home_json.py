import json

dict_ = {}  # создаём пустой словарь
while True:  # запускаем цикл, чтобы записать покупки и стоимость
    user_product = input('Введите название покупки, а чтобы выйти "стоп":')
    user_price = int(input('Введите стоимость покупки: '))
    if user_product == 'стоп':  # цикл прерывается при введении "стоп"
        break
    dict_.setdefault(user_product, user_price)  # метод возвращает в пустой словарь ключ: значение


with open('product.json', 'w', encoding='UTF-8') as file:  # открыли файл в режиме записи
    json.dump(dict_, file, ensure_ascii=False)  # записываем объект в наш json-файл


# exercise_2
with open('product.json', 'r', encoding='UTF-8') as file_1:
    product = json.load(file_1)
print(sum(product.values()))  # сумма покупок





