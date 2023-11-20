import cx_Oracle
import pandas
import datetime
#con = cx_Oracle.connect("python", "python", "localhost")

def insert10man():
    
    con = cx_Oracle.connect('python/python@localhost:1521/xe')
    cur = con.cursor()
    
    for i in range(1,100000+1):
        
        col01 = i
        col02 = i % 100
        col03 = i % 100
        col04 = i % 100
        
        sql = f"""INSERT into stress(col01, col02, col03, col04) VALUES({col01}, '{col02}', '{col03}', '{col04}')"""
        cur.execute(sql)
        print(cur.rowcount)

# df= pandas.read_sql(sql, con =con)

    con.commit()

# cur.fetchall()
# print(df)
    cur.close()
    con.close()

bef = datetime.datetime.now()
insert10man()
aft = datetime.datetime.now()

ell = aft - bef
print(ell)