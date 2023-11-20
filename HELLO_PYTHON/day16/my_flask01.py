from flask import Flask
from flask.templating import render_template
from flask.json import jsonify
from flask.globals import request
from day16.daoemp import DaoEmp

app = Flask(__name__)
de = DaoEmp()

@app.route('/')
@app.route('/emp')
def emp():
    return render_template('emp.html')

@app.route('/myajax', methods=['POST'])
def myajax():
    params = request.form['menu']
    print(params)
    
    return jsonify({'msg':'ok'})

@app.route('/mylist', methods=['POST'])
def mylist():
    
    list = de.selectList()
    print(list)
    
    return jsonify({'list': list})

@app.route('/myone', methods=['GET','POST'])
def myone():
    params = request.form['e_id']
    emp = de.selectOne(params)
    
    print("emp",emp)
    return jsonify({'emp': emp[0]})

@app.route('/mymod', methods=['GET','POST'])
def mymod():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    gen = request.form['gen']
    addr = request.form['addr']
    
    cnt = de.update(e_id, e_name, gen, addr)
    return jsonify({'cnt': cnt})

@app.route('/mydel', methods=['GET','POST'])
def mydel():
    e_id = request.form['e_id']
    
    cnt = de.delete(e_id)
    
    return jsonify({'cnt': cnt})

@app.route('/myadd', methods=['GET','POST'])
def myadd():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    gen = request.form['gen']
    addr = request.form['addr']
    
    cnt = de.insert(e_id, e_name, gen, addr)
    return jsonify({'cnt': cnt})

if __name__ == '__main__':
    #app.run('127.0.0.1', 5000, debug=True)
    app.run(debug=True)