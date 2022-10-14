a = 2
a = a / 0.5
# a -> 1
print(a)
print(type(a))    # к какому классу относится (int - числовой)
print(id(a))    # идентификатор (ячейка памяти) - адрес в памяти


_apple = 1
apple = 2
apple1223 = 2    # не начинать переменную с цифры


int()   # integer
float()   # вещественные числа(0.1, 5.7)
str()   # строка string
bool()   # true // false

k = 12312
s = str(k)   # преобразовать к строке
r = int(s)   # вернуться к числу
print(s, type(s))

