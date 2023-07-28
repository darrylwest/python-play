#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-28 13:36:56

import begin
from typing import TypedDict
from collections import namedtuple

class Config(TypedDict):
    env: str
    name: str
    port: int
    weight: float
    version: str

AppConfig = namedtuple('AppConfig', 'env name port weight version')

def create_config():
    c: Config = {
        'env': 'develop',
        'name': 'AppConfig',
        'port': 4040,
        'weight': 4.32,
        'version': '1.0.4',
    }

    return AppConfig(c['env'], c['name'], c['port'], c['weight'], c['version'])

@begin.start
def main(arg1 = None):
    cfg = create_config()

    print(f'config {cfg}')
    print(cfg.name)

    # cfg.env = "prod"
    # print(cfg, cfg.env)
