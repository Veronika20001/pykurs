def give_sum(a, b):  # задаём !параметры! в скобках
    pass


def give_minus(a, b):
    pass


def give_multi(a, b):
    pass


def give_division(a, b):
    pass


give_sum()
give_minus()
give_multi()
give_division()


# exersice_1
def sum_():
    arr_ = [1, 2, 3, 4, 5]
    print(sum(arr_))


sum_()


# на високосный год
def is_year_leap(year):
    if year % 4 == 0 or year % 400 == 0 and year % 100 == 0:
        return True
    else:
        return False


print(is_year_leap(1988))


# exersice
def func(w, r):
    global a
    a = w * r
    return a


def wert():
    return a ** 2


func(1, 4)
print(wert())