import pymysql
db = pymysql.connect(host='localhost', port=3305, user='root', passwd='python', db='python', charset='utf8')

sql = "DELETE from emp WHERE e_id = %s"
# sql = f"""DELETE from emp"""

curs = db.cursor()

cnt = curs.execute(sql)

print(cnt)

db.commit()
curs.close()
db.close()
