import rgbcontroller.lighting_effects as le

from threading import Lock

effects_list = dict(le.effects)
for i in effects_list:
    effects_list[i].pop('function', None)

state_lock = Lock()

state = {
    "current_effect": "off",
    "speed": 0,
    "brightness": 0,
    "color": "#000000"
}