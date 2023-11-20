from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/bingo')
def bingo():
    return render_template('bingo.html')

if __name__ == '__main__':
    # app.run('127.0.0.1', 5000, debug=True)
    app.run(debug=True)