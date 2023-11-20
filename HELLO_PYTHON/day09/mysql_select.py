import pymysql
db = pymysql.connect(host='localhost', port=3305, user='root', passwd='python', db='python', charset='utf8')

sql = "SELECT e_id as e_id,e_name,gen,addr FROM emp"

curs = db.cursor()

# with db:
#     with db.cursor() as cursor:
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         for data in result:
#             print(data)

curs.execute(sql)
rows = curs.fetchall()
print(rows)

db.close()
