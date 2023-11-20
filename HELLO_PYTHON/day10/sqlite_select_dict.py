import sqlite3
conn = sqlite3.connect("python.db")

curs = conn.cursor()
sql = "select * from mem"
curs.execute(sql)

mlist = []

rows = curs.fetchall()
for r in rows:
    mlist.append({'m_id':r[0],'m_name':r[1],'tel':r[2],'address':r[3]})
    
print(mlist)

curs.close()
conn.close()