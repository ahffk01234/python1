import pymysql
db = pymysql.connect(host='localhost', port=3305, user='root', passwd='python', db='python', charset='utf8')

sql = "UPDATE emp SET e_name ='5',gen = '5' ,addr = '5'  WHERE e_id = 3"
#sql = f"""UPDATE emp SET e_name ='{e_name}',gen = '{gen}' ,addr = '{addr}'  WHERE e_id = '{e_id}'"""

# sql = "UPDATE emp SET e_name = %s,gen = %s,addr = %s  WHERE e_id = 3"
curs = db.cursor()

cnt = curs.execute(sql)
# cnt = curs.execute(sql, ('5','5','5'))

db.commit()
curs.close()
db.close()
