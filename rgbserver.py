#!/bin/python3

from flask import Flask, render_template, jsonify, request
from threading import Thread
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/set_effect", methods=['POST'])
def set_effect():
    effect_json = request.get_json()
    print(effect_json)
    print(effect_json['effect'])
    return '',204

def start_lights():
    while True:
        print("showing light effect")
        time.sleep(1)

server_thread = Thread(target = lambda: app.run(host="0.0.0.0", port="8080"))
server_thread.start()

light_thread = Thread(target= lambda: start_lights())
light_thread.start()
