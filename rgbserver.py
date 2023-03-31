#!/bin/python3

from flask import Flask, render_template, jsonify, request
from threading import Thread
import time
import lighting_effects as le
import json

current_effect = 0

app = Flask(__name__)

effects_list = dict(le.effects)

for i in effects_list:
    effects_list[i].pop('function', None)

print(json.dumps(effects_list))

@app.route("/")
def index():
    print(le.effects.keys())
    return render_template("index.html", len = len(le.effects), effects_keys = list(le.effects.keys()), effects = le.effects, effects_string = effects_list)

@app.route("/set_effect", methods=['POST'])
def set_effect():
    effect_json = request.get_json()    
    return '',204

def start_lights():
    while True:
        time.sleep(1)

server_thread = Thread(target = lambda: app.run(host="0.0.0.0", port="8080"))
server_thread.start()

light_thread = Thread(target= lambda: start_lights())
light_thread.start()
