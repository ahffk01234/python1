import sqlite3

class DaoMem:
    def __init__(self):
        self.conn = sqlite3.connect('python.db')
        self.curs = self.conn.cursor()
        
    def selectList(self):
        self.curs.execute("SELECT * FROM mem")
        mlist = []
        mem = self.curs.fetchall()
        for m in mem:
            mlist.append({'m_id':m[0],'m_name':m[1],'tel':m[2],'address':m[3]})
        return mlist

    def selectOne(self,m_id):
        sql = f"""
            select
                m_id,m_name,tel,address
             from mem
            where 
                m_id = {m_id}
        """
        self.curs.execute(sql)
        mems = self.curs.fetchall()
        m = mems[0]
        return({'m_id':m[0],'m_name':m[1],'tel':m[2],'address':m[3]})
        
    
    
if __name__ == '__main__':
    dm = DaoMem()
    vo = dm.selectList()
    print(vo)        
        
        
        
        