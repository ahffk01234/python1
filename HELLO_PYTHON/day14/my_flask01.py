from flask import Flask
from flask.templating import render_template
from day14.daomem import DaoMem

app = Flask(__name__)
de = DaoMem()

@app.route('/')
@app.route('/mem_list')
def emp():
    mem = de.selectList()
    return render_template('mem_list.html',mem=mem)


if __name__ == '__main__':
    app.run(debug=True)