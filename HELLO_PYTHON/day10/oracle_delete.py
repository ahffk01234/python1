import cx_Oracle
import pandas
con = cx_Oracle.connect('python/python@localhost:1521/xe')
#con = cx_Oracle.connect("python", "python", "localhost")
e_id = 3
sql = f"""delete from emp where e_id = {e_id}"""
cur = con.cursor()

# df= pandas.read_sql(sql, con =con)

cur.execute(sql)

print(cur.rowcount)

con.commit()
# print(df)
cur.close()
con.close()