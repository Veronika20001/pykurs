import sqlite3

conn = sqlite3.connect('example1.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS 
tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, 
col_1 INTEGER, 
col_2 TEXT, 
col_3 TEXT
)
''')

us_int = int(input('Введите число для 1 колонки: '))


cursor.execute('''INSERT INTO tab_1(col_1, col_2, col_3) VALUES(?, 'hello', 'world')''', (us_int,))
conn.commit()

cursor.execute('''SELECT * FROM tab_1''')
print(cursor.fetchall())