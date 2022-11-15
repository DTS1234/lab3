from threading import Thread
from flask import Flask
import requests
from time import sleep
from threading import Thread

app = Flask(__name__)

BOX = None

def retrieve_box():
    global BOX

    while True:

        if not BOX:
            res = requests.get("http://service1:18888/")
            BOX = res.text
            
        sleep(30)

@app.before_first_request
def run_thread():
    Thread(target=retrieve_box).start()
    

@app.route("/", methods=["GET"])
def open_box():
    global BOX

    box = BOX
    BOX = None

    return box if box else ""