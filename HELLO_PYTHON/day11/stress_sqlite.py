import sqlite3
import datetime

def delete():
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
    
def insert10man():
    
    conn = sqlite3.connect("stress.db")
    curs = conn.cursor()
    
    for i in range(1,100000+1):
        
        col01 = i
        col02 = i % 100
        
        # sql = f"""INSERT into stress(col01, col02, col03, col04) VALUES('{col01}', '{col02}', '{col02}', '{col02}')"""
        sql = "insert into stress (col01, col02, col03, col04) values (?,?,?,?)"
        # curs.execute(sql)
        curs.execute(sql, (col01, col02, col02, col02))


# for i in range(1,5):
    # curs.execute(sql,(i,i,i,i))

        # cnt = curs.rowcount

    # sql1 = "select * from mem"

    # print(cnt)

    conn.commit()
    curs.close()
    conn.close()
    
bef = datetime.datetime.now()
insert10man()
aft = datetime.datetime.now()

ell = aft - bef
print(ell)