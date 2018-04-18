import sqlite3

connection = sqlite3.connect("ksiazki.db")
cursor = connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS ksiazki (id integer, title text, publishing text, year integer) ''')

cursor.execute('''INSERT INTO ksiazki VALUES (2, 'Maze Runner', 'Insignis', 2012)''')

connection.rollback()

for row in cursor.execute('''SELECT * FROM ksiazki'''):
    print row

connection.close()