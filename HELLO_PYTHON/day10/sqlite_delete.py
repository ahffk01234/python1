import sqlite3
conn = sqlite3.connect("stress.db")

sql = "delete from stress"

curs = conn.cursor()
curs.execute(sql)

cnt = curs.rowcount

# sql1 = "select * from emp"

# curs.execute(sql1)

# print(curs.fetchall())

print(cnt)

conn.commit()
curs.close()
conn.close()