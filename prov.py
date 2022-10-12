# exersice_2
def square_circle(r):
    return 3.14 * (r ** 2)


def square_triangle(a, h):
    return 0.5 * a * h


def square_rectangle(a, b):
    return a * b


def square_():
    user_choice = input('Введите, площадь чего хотите вычислить (треугольник, круг, прямоугольник): ')
    if user_choice == 'треугольник':
        print(square_triangle(int(input('Введите длину основания: '), int(input('Введите высоту')))))
    elif user_choice == 'круг':
        print(square_circle(int(input('Введите радиус: '))))
    elif user_choice == 'прямоугольник':
        print(square_rectangle(int(input('Введите длину высоты: '), int(input('Введите длину ширины')))))
    else:
        print('Введено неверно')


square_()
