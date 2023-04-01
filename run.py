from rgbcontroller import create_app, socketio, lighting_effects
from threading import Thread

app = create_app()

lighting_effects.start_lighting()