import cx_Oracle
import pandas
con = cx_Oracle.connect('python/python@localhost:1521/xe')
#con = cx_Oracle.connect("python", "python", "localhost")

e_id = 3
e_name ='3'
gen = '3'
addr = '3'

sql = f"""insert into emp(E_ID, E_NAME, GEN, ADDR) values({e_id},{e_name},{gen},{addr})"""

cur = con.cursor()

# df= pandas.read_sql(sql, con =con)

cur.execute(sql)

# cur.fetchall()
print(cur.rowcount)
con.commit()
# print(df)
cur.close()
con.close()