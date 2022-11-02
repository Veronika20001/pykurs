class Example:
    dig_1 = 1
    dig_2 = 2

    def __init__(self, dig_3, dig_4):
        self.dig_3 = dig_3
        self.dig_4 = dig_4

    def func_1(self):
        m = 88
        print(m)

    def func_2(self):
        return Example.dig_1 + Example.dig_2

    def func_3(self):
        return self.dig_3 ** self.dig_4

obj = Example(6, 9)
obj.func_1()
print(obj.func_2())
print(obj.func_3())

# exercise_2
class Calculator:

    def __init__(self):
        self.dig_1 = int(input('Введите первое число:'))
        self.dig_2 = int(input('Введите второе число: '))

    def sum(self):
        return self.dig_1 + self.dig_2

    def difference(self):
        return self.dig_1 - self.dig_2

    def multiplication(self):
        return self.dig_1 * self.dig_2

    def division(self):
        try:
            return self.dig_1 / self.dig_2
        except ZeroDivisionError:
            return 'Деление на 0!'

    def main(self):
        print(self.sum(), self.difference(), self.multiplication(), self.division(), sep='\n')

obj = Calculator()
obj.main()

# homework
class Str_or_int:
    vowels = []
    consonants = []

    def __init__(self):
        self.user_input = input('Введите строку или число: ')

    def length(self):
        self.len_string = len(self.user_input)
        return f'Длина вводимой строки = {self.len_string}'

    def isstring_(self):
        if self.user_input.isalpha():
            for i in self.user_input:
                if i in 'ауоиэыяюеё':
                    Str_or_int.vowels.append(i)
                elif i in 'цкжнгшбщзхйвпрлдчсмтф':
                    Str_or_int.consonants.append(i)
            if len(Str_or_int.vowels) * len(Str_or_int.consonants) <= self.len_string:
                return Str_or_int.vowels
            else:
                return Str_or_int.consonants
        elif self.user_input.isdigit():
            sum_even = sum([int(y) for y in list(self.user_input) if int(y) % 2 == 0])
            return sum_even * self.len_string


    def main_(self):
        print(self.length(), self.isstring_(), sep='\n')


obj = Str_or_int()
obj.main_()
