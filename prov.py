def date_():
    month_ = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
              'ноябрь', 'декабрь']
    month_30_days = ['апрель', 'июнь', 'сентябрь', 'ноябрь']
    month_31_days = ['январь', 'март', 'май', 'июль', 'август', 'октябрь']
    new_month = ''
    if day == 31 and month == 'декабрь':
        print('1 января', year + 1)
    if month == 'февраль':
        if day == 28 and year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print('29 февраля', year)
        else:
            print('1 марта', year)
    if day == 30 and month in month_30_days or day == 31 and month in month_31_days:
        for index, value in enumerate(month_):
            if value == month:
                new_month = month_[index + 1]
        print('1', new_month, year)
    else:
        print(day + 1, month, year)


day = int(input('Введите день: '))
month = input('Введите месяц: ')
year = int(input('Введите год: '))

date_()