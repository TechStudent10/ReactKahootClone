from flask import Flask, request
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret!"
socketio = SocketIO(app)
client = MongoClient()
app.debug = True

db = client.ReactKahootClone

games = db.games
currently_playing = db.current_playing

@socketio.on("join_room")
def join_room(data):
    username = data['username']
    room_code = data['room_code']
    room = currently_playing.find_one({'_id': room_code})
    if room:
        join_room(room_code)
        send(room, json=True)
        emit('join', {'username': username}, room=room_code)
        print(username, "has joined a room with room code:", room_code)
    else:
        emit('error', {'error': 'Room not found'})

if __name__ == "__main__":
    socketio.run(app)