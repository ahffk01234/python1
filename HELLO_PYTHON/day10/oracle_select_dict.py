import cx_Oracle
import pandas
con = cx_Oracle.connect('python/python@localhost:1521/xe')
#con = cx_Oracle.connect("python", "python", "localhost")
sql = "select * from emp"
cur = con.cursor()

# df= pandas.read_sql(sql, con =con)

cur.execute(sql)
rows = cur.fetchall()
list = []
for r in rows:
    list.append({'e_id':r[0],'e_name':r[1],'gen':r[2],'addr':r[3]})
    
print(list)


# print(df)
cur.close()
con.close()