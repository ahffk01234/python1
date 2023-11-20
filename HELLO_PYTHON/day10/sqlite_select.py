import sqlite3
conn = sqlite3.connect("python.db")

curs = conn.cursor()
sql = "select * from mem"
curs.execute(sql)
print(curs.fetchall())

curs.close()
conn.close()
