import os
from flask import Flask

server = Flask(__name__)

@server.route('/')
def listBlog():
    return '<div>Hello Trento</div>'
if __name__ == '__main__':
    server.run()
