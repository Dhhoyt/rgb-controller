#!/bin/python3

from flask import Flask, render_template, jsonify, request
from threading import Thread, Lock
import time
import lighting_effects as le
import json

state = {
    "current_effect": "off",
    "speed": 0,
    "brightness": 0,
}

state_lock = Lock()

app = Flask(__name__)

effects_list = dict(le.effects)

for i in effects_list:
    effects_list[i].pop('function', None)

print(json.dumps(effects_list))

@app.route("/")
def index():
    return render_template("index.html", len = len(le.effects), effects_keys = list(le.effects.keys()), effects = le.effects, effects_config = effects_list, state=state)

@app.route("/set_effect", methods=['POST'])
def set_effect():
    with state_lock:
        effect_json: dict = request.get_json()
        if "effect" in effect_json:
            effect_name = effect_json['effect']
            if effect_name in effects_list:
                state['current_effect'] = effect_name
                return '',204
            else:
                return f"Effect {effect_name} not a valid effect name.",400
        return '',204

@app.route("/state", methods=['GET'])
def get_state():
    with state_lock:
        return jsonify(state)

def start_lights():
    while True:
        time.sleep(1)

server_thread = Thread(target = lambda: app.run(host="0.0.0.0", port="8080"))
server_thread.start()

light_thread = Thread(target= lambda: start_lights())
light_thread.start()
