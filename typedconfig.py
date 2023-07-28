#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-28 13:36:56

import begin
from typing import TypedDict

class Config(TypedDict):
    port: int
    name: str
    weight: float
    version: str

def create_config():
    conf: Config = {
        'port': 4040,
        'name': 'AppConfig',
        'weight': 4.32,
        'version': '1.0.4',
    }

    return conf

@begin.start
def main(arg1 = None):
    cfg = create_config()

    print(f'config {cfg}')
