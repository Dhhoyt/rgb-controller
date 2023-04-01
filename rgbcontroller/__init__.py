from flask import Flask 
from flask_socketio import SocketIO 

from .events import socketio
from .routes import main 

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = False
    app.config["SECRET_KEY"] = "secret"

    app.register_blueprint(main)

    socketio.run(app, async_mode='gevent', host="0.0.0.0", port=8080)