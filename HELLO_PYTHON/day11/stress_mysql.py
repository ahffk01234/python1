import pymysql
import datetime


def insert10man():
    
    db = pymysql.connect(host='localhost', port=3305, user='root', passwd='python', db='python', charset='utf8')
    curs = db.cursor()
    
    for i in range(1,100001):
        
        col01 = i
        col02 = i % 100
        col03 = i % 100
        col04 = i % 100
        
        sql = f"""INSERT into stress(col01, col02, col03, col04) VALUES({col01}, '{col02}', '{col03}', '{col04}')"""

        cnt = curs.execute(sql)

    db.commit()
    curs.close()
    db.close()
    
bef = datetime.datetime.now()
insert10man()
aft = datetime.datetime.now()

ell = aft - bef
print(ell)