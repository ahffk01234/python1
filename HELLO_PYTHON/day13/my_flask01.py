from flask import Flask
from flask.globals import request
from flask.templating import render_template
from day13.daoemp import DaoEmp

app = Flask(__name__)
de = DaoEmp()

@app.route('/')
@app.route('/emp_list')
def emp():
    list = de.selectList()
    return render_template('emp_list.html', list=list)

@app.route('/emp_insert')
def emp_insert():
    return render_template('emp_insert.html')

@app.route('/emp_insert_act',methods=['POST'])
def insert():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    gen = request.form['gen']
    addr = request.form['addr']
    
    cnt = de.insert(e_id, e_name, gen, addr)
    
    return render_template('emp_insert_act.html',cnt=cnt)

@app.route('/detail')
def detail():
    e_id = request.args.get('e_id')
    print(e_id)
    emp = de.selectOne(e_id)
    print(emp)
    return render_template('emp_detail.html',emp=emp)

@app.route('/emp_mod')
def emp_mod():
    e_id = request.args.get('e_id')
    emp = de.selectOne(e_id)
    return render_template('emp_mod.html' , emp=emp)

@app.route('/emp_mod_act', methods=['POST'])
def emp_mod_act():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    gen = request.form['gen']
    addr = request.form['addr']
    
    print("e_id",e_id,"e_name",e_name,"gen",gen,"addr",addr)
    cnt = de.update(e_id, e_name, gen, addr)
    return render_template('emp_mod_act.html', cnt=cnt)


@app.route('/delete',methods=['GET'])   
def delete():
    e_id = request.args.get('e_id')
    print(e_id)
    cnt = de.delete(e_id)
    return render_template('emp_del_act.html',cnt=cnt)

if __name__ == '__main__':
    app.run(debug=True)