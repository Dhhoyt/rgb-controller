from PIL import ImageColor
from .state import state_lock, state
import time
import board
import neopixel

def off():
    pass

def rainbow():
    pass

def start_lighting():
    pixels = neopixel.NeoPixel(board.D12, 146)
    while True:
        print("jee")
        our_state = {}
        with state_lock:
            our_state = dict(state)
            our_state['color'] = ImageColor.getcolor(state['color'], "RGB")
        print(our_state)
        pixels.fill(our_state['color'])
        time.sleep(1)

effects = {
    "off": {
        "function": off,
        "display": "Off",
        "controls": [],
    },
    "rainbow": {
        "function": rainbow,
        "display": "Rainbow",
        "controls": ["SPEED"],
    }
}


effects_list = dict(effects)
for i in effects_list:
    effects_list[i].pop('function', None)