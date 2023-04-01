from flask import request
from flask_socketio import emit
from .extensions import socketio
from .state import state, state_lock, effects_list
import regex as re
import json

HEX_COLOR_REGEX = re.compile(r'^#[A-Fa-f0-9]{6}$')

@socketio.on("change_state")
def handle_new_message(message):
    effect_json: dict = json.loads(message)
    with state_lock:
        if "effect" in effect_json:
            effect_name = effect_json['effect']
            if effect_name in effects_list:
                state['current_effect'] = effect_name
        if "color" in effect_json:
            color = effect_json['color']
            if HEX_COLOR_REGEX.search(color):
                state['color'] = color
        if "speed" in effect_json:
            speed = effect_json['speed']
            if speed.isdigit():
                state['speed'] = speed
        if "brightness" in effect_json:
            brightness = effect_json['brightness']
            if brightness.isdigit():
                state['brightness'] = brightness
    emit("state_changed", state, broadcast=True)