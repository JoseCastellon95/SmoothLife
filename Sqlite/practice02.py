import sqlite3

con = sqlite3.connect("practice.db")

c = con.cursor()

user_input = int(input("Indroduce un numero: "))

c.execute('''CREATE TABLE IF NOT EXISTS numb(ID PRIMARY KEY AUTOINCREMENT,n int)''')

c.execute('INSERT INTO numb values(?)',(user_input,))


con.commit()
con.close()