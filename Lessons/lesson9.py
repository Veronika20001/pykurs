from random import *

list_ = [randint(1, 100) for i in range(10)]
tup = tuple(list_)
print(max(tup), min(tup))


list_1 = [randint(1, 5) for i in range(10)]
list_2 = [randint(-5, 0) for x in range(10)]
tuple_1 = tuple(list_1)
tuple_2 = tuple(list_2)
new_tuple = list_1 + list_2
zero = new_tuple.count(0)
print(f'Кортеж: {new_tuple}, количество нулей в нём: {zero}')


tuple_1 = ('string', 'sun', 'snow')
print(*tuple_1, sep=',') # * распаковка символа
