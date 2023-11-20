import sqlite3


class DaoMem:

    def __init__(self):
        self.conn = sqlite3.connect('mem.db', check_same_thread=False)
        self.curs = self.conn.cursor()
        
    def selectList(self):
        self.curs.execute("SELECT m_id, m_name, age, height FROM member")
        mlist = []
        mem = self.curs.fetchall()
        for m in mem:
            mlist.append({'m_id':m[0], 'm_name':m[1], 'age':m[2], 'height':m[3]})
        return mlist

    def insert(self, m_id, m_name, age, height):
        self.curs.execute(f"insert into member(m_id,m_name,age,height) values({m_id},{m_name},{age},{height})")
        self.conn.commit()
        return self.curs.rowcount
    
    def update(self, m_id, m_name, age, height):
        self.curs.execute(f"update member set m_name={m_name}, age={age}, height={height} where m_id={m_id}")
        self.conn.commit()
        return self.curs.rowcount
    
    def delete(self, m_id):
        self.curs.execute(f"delete from member where m_id={m_id}")
        self.conn.commit()
        return self.curs.rowcount
    
    def selectOne(self, m_id):
        self.curs.execute(f"select * from member where m_id={m_id}")
        m = self.curs.fetchall()[0]
        return  {'m_id':m[0], 'm_name':m[1], 'age':m[2], 'height':m[3]}

        
if __name__ == '__main__':
    dm = DaoMem()
    vo = dm.selectOne(3)
    print(vo)        
        
        
