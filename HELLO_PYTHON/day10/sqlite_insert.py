import sqlite3
conn = sqlite3.connect("python.db")

sql = "insert into mem(m_id,m_name,tel,address) values(?,?,?,?)"

curs = conn.cursor()

for i in range(1,5):
    curs.execute(sql,(i,i,i,i))

cnt = curs.rowcount

sql1 = "select * from mem"

curs.execute(sql1)

print(curs.fetchall())

print(cnt)

conn.commit()
curs.close()
conn.close()