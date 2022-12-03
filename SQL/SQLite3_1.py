import sqlite3

# создаём базу данных, подключение к бд
conn = sqlite3.connect('name.db')
# инициализируем курсор(каретка) помогает взаимодействовать с бд
cursor = conn.cursor()
# создаём таблицу,
# указывая название таблицы,
# указываем название id - по нему будут настраиваться связи между таблицами
# кнопки будут col_1 и col_2 текстовыми
cursor.execute('''
    CREATE TABLE IF NOT EXISTS 
    tab_1(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    col_1 TEXT,
    col_2 TEXT
    )
''')
# заполняем нашу таблицу
# 1, указываем конструкцию INSERT INFO
# 2. указываем в какие поля

cursor.execute('''
    INSERT INTO tab_1(col_1, col_2) 
    VALUES('hello', 'world')
''')

# сохранение изменений
conn.commit()

# заполнение таблицы с помощью данных, получаемых из переменных, 3 колонки
cursor.execute('''
    CREATE TABLE IF NOT EXISTS
    tab_2(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col_1 TEXT,
    col_2 TEXT
    )
''')

var1 = 'red'
var2 = 'black'

command = '''
    INSERT INTO tab_2(col_1, col_2)
    VALUES(?,?)
'''

cursor.execute('''
    INSERT INTO tab_2(col_1, col_2)
    VALUES(?,?)
''', (var1, var2))

data_list = [('yellow', 'white') for x in range(10)]

for tuple_ in data_list:
    cursor.execute(command, tuple_)

# сохраняем
conn.commit()

# задание
for i in range(10):
    us_col_1 = input('Введите значение для 1 колонки:')
    us_col_2 = input('Введите значение для 2 колонки:')
    cursor.execute('''
        INSERT INTO tab_2(col_1, col_2)
        VALUES(?,?)''', (us_col_1, us_col_2))

conn.commit()

cursor.execute('''SELECT * FROM tab_2''')

print(cursor.fetchall())
