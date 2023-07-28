#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-28 13:36:56

import begin
from typing import TypedDict
from collections import namedtuple

def notes():
    s = """
    _____________________________________________________________________________________________________

    This prototype creates an immutable namedtuple with the typed fields.

    It's kind of overkill to have both, so it should probably be reduced to just the named tuple to 
    ensure 1) immutability, and 2) dot-access in the app.

    Config Requirements:

        1) support multiple environments (devop, test, staging, prod)
        2) be type-safe
        3) immutable
        4) versioned
        5) dot-friendly
        6) support methods that pull config settings from secret locations (apikeys, db passwords, etc)

    Config Alternatives:

        1) config parser - file-based config; error prone and not type-safe
        2) type dictionary - typed good, mutable bad
        3) custom classes - ok, but namedtuple is an easier way 
        4) dataclass - mutable

    dpw | 28-Jul-2023
    _____________________________________________________________________________________________________
    """

    print(s)

class Config(TypedDict):
    env: str
    name: str
    port: int
    weight: float
    version: str

AppConfig = namedtuple('AppConfig', 'env name port weight version apikey dbpw')

def apikey(env):
    return f'{env}-*******'

def dbpw(env):
    return f'{env}-*******'

def create_config():
    cfg: Config = {
        'env': 'develop',
        'name': 'AppConfig',
        'port': 4040,
        'weight': 4.32,
        'version': '1.0.4',
    }

    return cfg

def create_app_config(cfg):
    return AppConfig(cfg['env'], cfg['name'], cfg['port'], cfg['weight'], cfg['version'],apikey,dbpw)

@begin.start
def main(arg1 = None):
    notes()

    cfg_dict = create_config()

    print(f'config {cfg_dict}')

    # this is mutable while just a typed dict
    cfg_dict['env'] = 'staging'

    cfg = create_app_config(cfg_dict)
    print(f'config:  {cfg}')
    print(cfg.name)

    print(f'apikey: {cfg.apikey(cfg.env)}, dbpw: {cfg.dbpw(cfg.env)}')

    # this will throw
    # cfg.env = "prod"
    # print(cfg, cfg.env)
