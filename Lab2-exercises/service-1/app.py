from flask import Flask
from flask import request

app = Flask(__name__)

WORDS = []
with open("file.txt", "r") as file:
    for line in file.readlines():
        WORDS.append(line.rstrip())
print(WORDS)
@app.route("/", methods=["GET"])
def open_box():
   return WORDS if len(WORDS) > 0 else ""


@app.route("/", methods=["POST"])
def fill_box():
    global BOX

    if BOX:
        return "Box is full", 400

    BOX = request.data

    return "OK", 200
