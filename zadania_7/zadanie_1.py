import sqlite3

connection = sqlite3.connect("ksiazki.db")
cursor = connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS ksiazki (id integer, title text, publishing text, year integer) ''')

cursor.execute('''INSERT INTO ksiazki VALUES (1, 'Metro 2033', 'Insignis', 2010)''')

connection.commit()

for row in cursor.execute('''SELECT * FROM ksiazki'''):
    print row

connection.close()