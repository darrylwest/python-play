#!/usr/bin/env python3.11
# dpw@Darryls-iMac.localdomain
# 2023-03-07 21:25:22
#

from rich import print
from flask import Flask, request

app = Flask(__name__)


@app.get("/")
def index():
    return "<p>hello world</p>"

@app.route('/log', methods=['POST'])
def handle_post():
    data = request.get_json()

    print(data)

    return 'ok'

@app.get("/what")
def what():
    return "<p>hello what?</p>"


if __name__ == "__main__":
    print("USE: FLASK_APP=webapp flask run")
