'''
Реализуйте итератор колоды карт (52 штуки) CardDeck.
Каждая карта представлена в виде строки типа «2 Пик».
При вызове функции next() будет представлена
следующая карта. По окончании перебора всех
элементов возникнет ошибка StopIteration.
'''


class CardDeck:
    def __init__(self, list_):
        self.list_ = list_
        self.mean = -1


    def __next__(self):
        if self.mean + 1 < len(self.list_):
            self.mean += 1
            return self.list_[self.mean]
        else:
            return StopIteration

list_cards = [
    'Туз Пик', '2 Пик', '3 Пик', '4 Пик', '5 Пик', '6 Пик', '7 Пик', '8 Пик', '9 Пик', '10 Пик',
    'Валет Пик', 'Дама Пик', 'Король Пик',

    'Туз Черва', '2 Черва', '3 Черва', '4 Черва', '5 Черва', '6 Черва', '7 Черва', '8 Черва', '9 Черва',
    '10 Черва', 'Валет Черва', 'Дама Черва', 'Король Черва',

    'Туз Бубен', '2 Бубен', '3 Бубен', '4 Бубен', '5 Бубен', '6 Бубен', '7 Бубен', '8 Бубен', '9 Бубен',
    '10 Бубен', 'Валет Бубен', 'Дама Бубен', 'Король Бубен',

    'Туз Треф', '2 Треф', '3 Треф', '4 Треф', '5 Треф', '6 Черва', '7 Треф', '8 Треф', '9 Треф', '10 Треф',
    'Валет Треф', 'Дама Треф', 'Король Треф'
]

card_ = CardDeck(list_cards)
for i in range(53):
    print(next(card_))



# итерация списка с ошибкой StopIteration
list_cards = [
    'Туз Пик', '2 Пик', '3 Пик', '4 Пик', '5 Пик', '6 Пик', '7 Пик', '8 Пик', '9 Пик', '10 Пик',
    'Валет Пик', 'Дама Пик', 'Король Пик',

    'Туз Черва', '2 Черва', '3 Черва', '4 Черва', '5 Черва', '6 Черва', '7 Черва', '8 Черва', '9 Черва',
    '10 Черва', 'Валет Черва', 'Дама Черва', 'Король Черва',

    'Туз Бубен', '2 Бубен', '3 Бубен', '4 Бубен', '5 Бубен', '6 Бубен', '7 Бубен', '8 Бубен', '9 Бубен',
    '10 Бубен', 'Валет Бубен', 'Дама Бубен', 'Король Бубен',

    'Туз Треф', '2 Треф', '3 Треф', '4 Треф', '5 Треф', '6 Черва', '7 Треф', '8 Треф', '9 Треф', '10 Треф',
    'Валет Треф', 'Дама Треф', 'Король Треф'
]

iterator_cards = iter(list_cards)
for i in range(53):
    print(next(iterator_cards))


# Итерация списка карт
cards = [
    'Туз Пик', '2 Пик', '3 Пик', '4 Пик', '5 Пик', '6 Пик', '7 Пик', '8 Пик', '9 Пик', '10 Пик', 'Валет Пик',
    'Дама Пик', 'Король Пик',

    'Туз Черва', '2 Черва', '3 Черва', '4 Черва', '5 Черва', '6 Черва', '7 Черва', '8 Черва', '9 Черва',
    '10 Черва', 'Валет Черва', 'Дама Черва', 'Король Черва',

    'Туз Бубен', '2 Бубен', '3 Бубен', '4 Бубен', '5 Бубен', '6 Бубен', '7 Бубен', '8 Бубен', '9 Бубен',
    '10 Бубен', 'Валет Бубен', 'Дама Бубен', 'Король Бубен',

    'Туз Треф', '2 Треф', '3 Треф', '4 Треф', '5 Треф', '6 Черва', '7 Треф', '8 Треф', '9 Треф', '10 Треф',
    'Валет Треф', 'Дама Треф', 'Король Треф'
]
for i in cards:  # выводит каждую карту в консоль
    print(i)
