from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/ttt')
def ttt():
    return render_template('ttt.html')

@app.route('/ttt5')
def ttt5():
    return render_template('tttx5.html')

if __name__ == '__main__':
    # app.run('127.0.0.1', 5000, debug=True)
    app.run(debug=True)