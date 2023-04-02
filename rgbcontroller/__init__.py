from flask import Flask 
from .events import socketio
from .routes import main 
from flask_socketio import SocketIO

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = False
    app.config["SECRET_KEY"] = "secret"

    app.register_blueprint(main)

    socketio = SocketIO(app, async_mode='gevent')

    socketio.run(app)
