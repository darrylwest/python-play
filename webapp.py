#!/usr/bin/env python3.11
# dpw@Darryls-iMac.localdomain
# 2023-03-07 21:25:22
#

from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return "<p>hello world</p>"


@app.get("/what")
def what():
    return "<p>hello what?</p>"

if __name__ == '__main__':
    print("USE: FLASK_APP=webapp flask run")
