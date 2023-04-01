from threading import Lock

state_lock = Lock()

state = {
    "current_effect": "off",
    "speed": 0,
    "brightness": 0,
    "color": "#000000"
}