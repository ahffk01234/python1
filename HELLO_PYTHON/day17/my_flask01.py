from flask import Flask
from flask.templating import render_template
from flask.json import jsonify
from flask.globals import request
from day17.daomem import DaoMem

app = Flask(__name__)
dm = DaoMem()


@app.route('/')
@app.route('/mem')
def mem():
    return render_template('mem.html')


@app.route('/memlist', methods=['POST'])
def mylist():
    
    list = dm.selectList()
    
    return jsonify({'list': list})


@app.route('/memOne', methods=['POST'])
def memOne():
    
    m_id = request.form['m_id']
    mem = dm.selectOne(m_id)
    
    return jsonify({'mem': mem})


@app.route('/insert', methods=['POST'])
def insert():
    
    m_id = request.form['m_id']
    m_name = request.form['m_name']
    age = request.form['age']
    height = request.form['height']
    
    cnt = dm.insert(m_id, m_name, age, height)
    return jsonify({'cnt': cnt})


@app.route('/update', methods=['POST'])
def update():
    m_id = request.form['m_id']
    m_name = request.form['m_name']
    age = request.form['age']
    height = request.form['height']
    
    cnt = dm.update(m_id, m_name, age, height)
    return jsonify({'cnt': cnt})


@app.route('/delete', methods=['POST'])
def delete():
    m_id = request.form['m_id']
    
    cnt = dm.delete(m_id)
    return jsonify({'cnt': cnt})


if __name__ == '__main__':
    # app.run('127.0.0.1', 5000, debug=True)
    app.run(debug=True)
