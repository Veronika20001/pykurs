import string

# exercise_1 (Cls Tomato)
class Tomato:
    states = {1: 'цветение', 2: 'формирование плода', 3: 'вызревание плода', 4: 'плод созрел'}

    def __init__(self, _index=1):
       self._index = _index
       self._state = Tomato.states.get(self._index)

    def grow(self):
        self._index += 1
        self._state = Tomato.states.get(self._index)

    def is_ripe(self):
        if self._state == 'плод созрел':
            return 'Томат достиг последней стадии созревания'
        else:
            return f'Томат на стадии {self._state}'


# exercise_2(cls TomatoBush)
class TomatoBush:

    def __init__(self, amount: int):
        self.tomatoes = []
        for i in range(1, amount + 1):
            i = Tomato()
            self.tomatoes.append(i)

    def grow_all(self):
        new_list = []
        for i in self.tomatoes:
            i.grow()
            new_list.append(i)
        self.tomatoes = new_list

    def all_are_ripe(self):
        if self.tomatoes[0].is_ripe():
            return True
        else:
            return False

    def give_away_all(self):
        self.tomatoes.clear()


# exercise_3(cls Gardener)
class Gardener:

    def __init__(self, name, _plant: TomatoBush):
        self.name = name
        self._plant = _plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Садовник собрал урожай')
        else:
            print('Ещё не все томаты созрели!')

        @staticmethod
        def knowledge_base(name_):
            print('Справка')


tomato_bush = TomatoBush(4)
Gard = Gardener('Sally', tomato_bush)

Gard.work()
Gard.work()
Gard.work()
Gard.work()
Gard.harvest()


# cls Human

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        f_discount = (self._price * discount) / 100
        f_price = self._price - f_discount
        return f_price

class SmallHouse(House):

    def_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.def_area, price)


class Human:
    # статистические поля(атрибуты класса)
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        # public
        self.name = name
        self.age = age
        # private
        self.__money = 5000
        self.__house = 'Minsk'

    def info(self):
        print(f'Name: {self.name}, age: {self.age}, house: {self.__house}, money: {self.__money}')

    @staticmethod
    def default_info():
        print(f'Default name: {Human.default_name}')
        print(f'Default age: {Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f'Earned {amount} money! Current value: {self.__money}')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('Недостаточно средств!')

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house



if __name__ == '__main__':

    rikky = Human('Rikky', 29)
    rikky.info()

    small_house = SmallHouse(10000)

    rikky.buy_house(small_house, 10)

    rikky.earn_money(5000)
    rikky.buy_house(small_house, 10)

    rikky.earn_money(20000)
    rikky.buy_house(small_house, 10)

    rikky.info()

# cls Alphabet

class Alphabet:

    def __init__(self, lang, letters : list):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    __letters_num = 26

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            print('Такая буква есть в алфавите!')
        else:
            print('Нет такой буквы в алфавите!')

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        return 'Hello, world!'


eng_ = EngAlphabet()
eng_.print()
print(eng_.letters_num())
eng_.is_en_letter('F')
eng_.is_en_letter('Щ')
print(eng_.example())