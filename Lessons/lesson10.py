dict_1 = {1: 5, 2: 3}
dict_2 = dict(one='1', two='2')
dict_3 = dict.fromkeys(['1', '2'], 5)
print(dict_1, dict_2, dict_3)

# удаление элемента del
salary = {'Director': 120800.0,
          'Secretary': 101150.25,
          'Locksmith': 188200.0}
print(salary)

del salary['Secretary']
print(salary)
key = 'Secretary'
if key in salary:
    del salary['Secretary']
    print(salary)

key2 = 5
if key2 in salary:
    del salary[key2]
    print(salary)

person = {'name': 'Andi',
          'age': 30,
          'city': 'Minsk'}
print(person)
print(person['age'])


car = dict(BMW=[7, 8, 9], Tesla=[1, 2, 3])
print(car['BMW'][0], car['BMW'][-1])
print(car['Tesla'][0], car['Tesla'][-1])
