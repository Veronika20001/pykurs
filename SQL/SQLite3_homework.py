import sqlite3

"""
Создать 2 таблицы в Базе Данных.
Одна будет хранить текстовые данные (1 колонка).
Другая числовые (1 колонка).
Есть список состоящий из чисел и слов.
Если элемент списка слово: записать его в соответствующую таблицу,
затем посчитать длину слова и записать ее в числовую таблицу
Если элемент списка число: проверить, если число чётное - записать его в таблицу чисел,
если нечётное, то записать во вторую таблицу слово: "нечётное".
Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице.
Если меньше 5, то обновить 1 запись в первой таблице на "hello"
"""

conn = sqlite3.connect('homework.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS 
tab_text(
id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 TEXT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS 
tab_int(
id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 INTEGER
)
""")

list_ = [1, 'sun', 'python', 8, 9, 7, 'sql',2, 'homework', 'execute']

for i in list_:
    if type(i) == str:
        cursor.execute('''INSERT INTO tab_text(col_1) VALUES(?)''', (i,))
        length = len(i)
        cursor.execute('''INSERT INTO tab_int(col_1) VALUES(?)''', (length,))
    elif type(i) == int:
        if i % 2 == 0:
            cursor.execute('''INSERT INTO tab_int(col_1) VALUES(?)''', (i,))
        elif i % 2 != 0:
            cursor.execute('''INSERT INTO tab_text(col_1) VALUES("нечётное")''')


conn.commit()
# cursor.execute('''SELECT * FROM tab_text''')
# print(cursor.fetchall())
cursor.execute('''SELECT * FROM tab_int''')
content_tab_int = cursor.fetchall()
# print(content_tab_int)

if len(content_tab_int) > 5:
    cursor.execute('''DELETE FROM tab_text WHERE id=1''')
else:
    cursor.execute('''UPDATE tab_text SET col_1="hello" ''')

cursor.execute('''SELECT * FROM tab_text''')
print(cursor.fetchall())
cursor.execute('''SELECT * FROM tab_int''')
print(cursor.fetchall())