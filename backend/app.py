from flask import Flask, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret!"
socketio = SocketIO(app)
app.debug = True

if __name__ == "__main__":
    socketio.run(app)