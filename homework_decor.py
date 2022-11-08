import logging

# homework
"""
Напишите декоратор debug, который при каждом вызове
декорируемой функции выводит её имя (вместе со всеми
передаваемыми аргументами), а затем — какое значение
она возвращает. После этого выводится результат её
выполнения
"""

def debug(func):

    def wrapper(variable_1, variable_2):
        print(func.__name__, variable_1, variable_2)
        return func(variable_1,variable_2)
    return wrapper

@debug
def variable(variable_1, variable_2):
    return variable_1 ** variable_2

print(variable(5,2))

# additional 'LIST'
list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # дан список
new_list_ = []
def decor(func):

    def wrapper(list_1):
        for i in list_1:
            for y in i:
                if y % 3 == 0:
                    new_list_.append(y)
        return new_list_
    return wrapper

@decor
def new_list(list_1):
    return len([x[a] for i in list_1 for x in range(3) if i[x] not in list_])

print(new_list(list_1))
