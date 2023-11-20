from flask import Flask, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)
app.secret_key = "mysecret"


socket_io = SocketIO(app)

@app.route('/')
def hello_world():
    return "Hello Gaemigo Project Home Page!!"

@app.route('/chat')
def chatting():
    return render_template('chat.html')

@app.route('/bingo_ws')
def bingo_ws():
    return render_template('bingo_ws.html')


@socket_io.on("message")
def request(message):
    print("message : "+ message)
    to_client = dict()
    to_client['message'] = message
    to_client['type'] = 'normal'
    # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)
    send(to_client, broadcast=True)



if __name__ == '__main__':
    socket_io.run(app,host="0.0.0.0", port=9999)

