from flask import Flask 

from .events import socketio
from .routes import main 

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = False
    app.config["SECRET_KEY"] = "secret"

    app.register_blueprint(main)

    socketio.init_app(app, async_mode="threading")

    return app