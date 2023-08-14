#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-08 17:43:25

import begin
import tomllib
from pprint import pprint as pp


def process():
    with open("data.toml", "rb") as f:
        data = tomllib.load(f)

    pp(data)


@begin.start
def main(arg1=None):
    process()
