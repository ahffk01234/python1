import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3305, user='root', passwd='python', db='python', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    def selectList(self):
        sql = "SELECT * FROM emp"
        self.curs.execute(sql)
        emps = self.curs.fetchall()
        return emps
    
    def selectOne(self,e_id):
        sql = f"""SELECT * FROM emp where e_id={e_id}"""
        self.curs.execute(sql)
        emp = self.curs.fetchall()
        return emp[0]
    
    def insert(self,e_id,e_name,gen,addr):
        sql = f"""INSERT into emp(e_id,e_name,gen,addr) VALUES('{e_id}', '{e_name}', '{gen}', '{addr}')"""
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self,e_id,e_name, gen, addr):
        sql = f"""UPDATE emp SET e_name ={e_name},gen = {gen} ,addr = {addr}  WHERE e_id = {e_id}"""
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self,e_id):
        sql = f"""DELETE from emp where e_id={e_id}"""
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
        
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    # emp = de.insert(5,5,5,5)
    # emp = de.update(4,5,5,5)
    de.seleltList()
