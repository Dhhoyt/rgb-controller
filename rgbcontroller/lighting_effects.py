from PIL import ImageColor
from .state import state_lock, state
import time
import board
import neopixel
import copy
import asyncio

def lerp_color(color1, color2, k):
    r = color1[0] * k + color2[0] * (1 - k)
    g = color1[1] * k + color2[1] * (1 - k)
    b = color1[2] * k + color2[2] * (1 - k)
    return (r,g,b)

async def off(pixels, our_state):
    pixels.fill((0, 0, 0))
    await asyncio.sleep(10)

async def rainbow(pixels, our_state):
    pass

async def static(pixels, our_state):
    pixels.fill(our_state['color'])
    await asyncio.sleep(10)

async def start_lighting():
    pixels = neopixel.NeoPixel(board.D12, 146)
    while True:
        print("jee")
        our_state = {}
        with state_lock:
            our_state = copy.deepcopy(state)
            our_state['color'] = ImageColor.getcolor(state['color'], "RGB")
        effect = effects[our_state['current_effect']]
        effect['function'](pixels, our_state)


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
    },
    "static": {
        "function": static,
        "display": "Static Color",
        "controls": []
    }
}


effects_list = copy.deepcopy(effects)
for i in effects_list:
    effects_list[i].pop('function', None)

print(effects)