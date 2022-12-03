import sqlite3
import random

conn = sqlite3.connect('example2.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS 
tab_1(
id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 INTEGER,
col_2 INTEGER
)
''')

rand_col_1 = random.randint(0, 9)
rand_col_2 = random.randint(0, 9)

cursor.execute('''INSERT INTO tab_1(col_1, col_2)
VALUES(?, ?)''', (rand_col_1, rand_col_2))

conn.commit()

cursor.execute('''SELECT col_1, col_2 FROM tab_1''')
col = cursor.fetchall()
print(col)

# осталось найти среднее арифметическое всех элементов таблицы, не включая id
# если ср ариф больше, чем кол-во записей, то удалить 4 запись
count = 0
list_ =[]
for i in col:
    for x in i:  # проходимся циклом кортежам внутри списка
        list_.append(x)
        count += x
average = count / len(list_)  # находим среднее арифметическое
# print(average)
if average > len(col):
    cursor.execute('''DELETE FROM tab_1 WHERE id = 4''')
conn.commit()

cursor.execute('''SELECT * FROM tab_1''')
print(cursor.fetchall())