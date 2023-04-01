from flask import Blueprint, render_template
from .state import state
from .lighting_effects import effects_list 

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html", len = len(effects_list), effects_keys = list(effects_list.keys()), effects = effects_list, state=state)