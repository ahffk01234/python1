import pymysql
db = pymysql.connect(host='localhost', port=3305, user='root', passwd='python', db='python', charset='utf8')

e_id = "3"
e_name = "3"
gen = "3"
addr = "3"
sql = f"""INSERT into emp(e_id,e_name,gen,addr) VALUES('{e_id}', '{e_name}', '{gen}', '{addr}')"""



curs = db.cursor()

cnt =curs.execute(sql)
print(cnt)

db.commit()
curs.close()
db.close()
