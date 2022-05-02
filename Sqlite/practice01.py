import sqlite3

con = sqlite3.connect("gta.db")

c = con.cursor()

gta = [(1997,"GRAND THEFT AUTO","State Of Guernsey"),
		(1999,"Grand Theft Auto II", "Anywhere, USA"),
		(2001,"Grad Theft Auto III","Liberty City"),
		(2002,"Grand Theft Auto: Vice City","Vice City"),
		(2004,"Grand Theft Auto: San Andreas","State Of San Andreas"),
		(2008,"Grand Theft Auto IV","Liberty City"),
		(2013,"Grand Theft Auto V","State Of San Andreas")
		]


c.execute(''' CREATE TABLE IF NOT EXISTS GTA (year INTEGER , name text , city text)''')


c.executemany('INSERT INTO GTA VALUES(?,?,?)', gta)

c.execute('SELECT * FROM GTA WHERE year=:year',{'year':1997})
year_search= c.fetchone()

print(year_search)




con.commit()
con.close()


