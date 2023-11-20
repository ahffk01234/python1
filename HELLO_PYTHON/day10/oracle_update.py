import cx_Oracle
import pandas
con = cx_Oracle.connect('python/python@localhost:1521/xe')
#con = cx_Oracle.connect("python", "python", "localhost")
sql = "update emp set e_name = '4',GEN='4', ADDR='4' where e_id = 3"
cur = con.cursor()

# df= pandas.read_sql(sql, con =con)

cur.execute(sql)

print(cur.rowcount)

con.commit()
# print(df)
cur.close()
con.close()