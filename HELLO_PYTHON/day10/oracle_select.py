import cx_Oracle
import pandas
con = cx_Oracle.connect('python/python@localhost:1521/xe')
#con = cx_Oracle.connect("python", "python", "localhost")
sql = "select * from emp"
cur = con.cursor()

# df= pandas.read_sql(sql, con =con)

cur.execute(sql)

print(cur.fetchall())

# print(df)
cur.close()
con.close()