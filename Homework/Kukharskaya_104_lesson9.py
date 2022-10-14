'''
Множества
'''

# exersice_1
list_ = [1, 3, 5, 7, 8, 9, 1, 4, 6]
set_1 = set(list_)
if list_ == set_1:
    print('Нет дубликатов в последовательности')
else:
    print('Есть дубликаты в последовательности')

# exersice_2
set_ = set([1, 3, 'joy', 5, 7, 'sun'])  # множество
frozenset_ = frozenset(['slow', 2, 3, 9, 'like'])  # неизменяемое множество
all_set = set_ | frozenset_  # объединение двух множеств

print(all_set)
print(set_ & frozenset_)  # пересечение элементов в двух множествах

# homework_1

list_ = [i for i in range(10)]
tuple_ = tuple(list_)
print(sum(tuple_))

# homework_2

long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
print(f'Количество "т": {long_word.count("т")}, Количество "а": {long_word.count("а")},'
      f' Количество "и": {long_word.count("и")}')

# homework_3

week_temp = (26, 29, 34, 32, 28, 26, 23)
sum_temp = sum(week_temp)
days = len(week_temp)
mean_temp = sum_temp / days
print(f'Средняя температура - {int(mean_temp)} градусов за {days} дней')
