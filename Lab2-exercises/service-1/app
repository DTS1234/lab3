from flask import Flask
from flask import request

app = Flask(__name__)

BOX = None

@app.route("/", methods=["GET"])
def open_box():
    global BOX

    box = BOX
    BOX = None

    return box if box else ""


@app.route("/", methods=["POST"])
def fill_box():
    global BOX

    if BOX:
        return "Box is full", 400

    BOX = request.data

    return "OK", 200