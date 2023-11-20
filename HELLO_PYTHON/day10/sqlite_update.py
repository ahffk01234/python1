import sqlite3
conn = sqlite3.connect("python.db")

sql = "update mem set m_name = ?, tel = ? ,address = ? where m_id = ?"

curs = conn.cursor()

curs.execute(sql,('3','3','3','2'))

cnt = curs.rowcount

sql1 = "select * from mem"

curs.execute(sql1)

print(curs.fetchall())

print(cnt)

conn.commit()
curs.close()
conn.close()