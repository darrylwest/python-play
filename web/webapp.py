#!/usr/bin/env python3.11
# dpw@Darryls-iMac.localdomain
# 2023-03-07 21:25:22
#

from flask import Flask, request
from rich import inspect, print

app = Flask(__name__)


@app.get("/")
def index():
    return "<p>hello world</p>"


@app.post("/v1/logit/<app>")
def logger(app):
    # data = request.args

    print(app)

    inspect(request.form)

    return "ok"


@app.get("/what")
def what():
    return "<p>hello what?</p>"


def main():
    print("starting")


if __name__ == "__main__":
    print("USE: FLASK_APP=web/webapp flask run -h 10.0.1.105 -p 6402")
