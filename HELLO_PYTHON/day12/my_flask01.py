from flask import Flask, request
from flask.templating import render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Flask!'

@app.route('/para')
def para():
    menu = request.args.get('menu')
    return f'PARA {menu}'

@app.route('/post', methods=['GET','POST'])
def mypost():
    menu = request.form['menu']
    return f'POST{menu}'

@app.route('/disfor')
def disfor():
    a = "잼버리"
    b = ["홍길동", "전우치", "이순신"]
    c = [
        {'e_id':'1','e_name':'1','gen':'1','addr':'1'},
        {'e_id':'2','e_name':'2','gen':'2','addr':'2'}
        ]
    return render_template('disfor.html', a=a, b=b, c=c)

@app.route('/emp')
def emp():
    
    db = pymysql.connect(host='localhost', port=3305,user='root', passwd='python', db='python', charset='utf8')
    cur = db.cursor(pymysql.cursors.DictCursor)
    
    sql = "SELECT * FROM emp"    
            
    cur.execute(sql)
    
    emps = cur.fetchall()
    print(emps)
    
    cur.close()
    db.close()
    
    
    return render_template('emp.html',emps=emps)
    
if __name__ == '__main__':
    #app.run('127.0.0.1', 5000, debug=True)
    app.run(debug=True)