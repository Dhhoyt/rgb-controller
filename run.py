from rgbcontroller import create_app, socketio, lighting_effects
from threading import Thread

app = create_app()

server_thread = Thread(target = lambda: app.run(host="0.0.0.0", port=8080))

lighting_thread = Thread(target = lambda: lighting_effects.start_lighting())

server_thread.start()
lighting_thread.start()