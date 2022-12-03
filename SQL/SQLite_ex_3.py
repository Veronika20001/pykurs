import sqlite3
import random

conn = sqlite3.connect('example3.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IN NOT EXISTS
tab_1(
id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 INTEGER,
col_2 INTEGER
)
''')
us_col_1 = random.randint(0, 9)
us_col_2 = random.randint(0, 9)

cursor.execute('''INSERT INTO
tab_1(col_1, col_2)
VALUES(?, ?)''', (us_col_1, us_col_2))

conn.commit()

cursor.execute('''SELECT * FROM tab_1''')
print(cursor.fetchall())
