# exersice1
from random import *
list_ = [randint(1, 20) for i in range(10)]
print(list_)
list_.reverse()
print(list_)

list_ = [randint(1, 20) for i in range(10)]
print(list_)
print(list_[::-1])

# exersice2
list_ = [1, 20, 5, 4, 66, 20]
list_[list_.index(20)] = 200
print(list_)




list_ = [
    [1, 2, 5, 1],
    [5, 8, 6, 7],
    [7, 7, 6, 1]
]

for i in list_:
    for x in i:
        print(x)


#
list_ = [
    [1, 2, 5, 1],
    [5, 8, 6, 7],
    [7, 7, 6, 1],
    123
]

for i in list_:
    for x in i:
        print(x)
# будет ошибка списки итерируемые, а число 123 не является!
for i in list_:
    if type(i) == list_:
        for x in i:
            print(x)

#
list_ = [
    [1, 2, 5, 1],
    [5, 8, 6, 7],
    [7, 7, 6, 1],
    123
]

for i in list_:
    if isinstance(i, list_):
        for x in i:
            print(x)

#
