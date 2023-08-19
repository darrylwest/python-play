#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-28 16:18:41

import sys
import time
from dataclasses import dataclass
from collections import namedtuple


def notes():
    s = """
    _____________________________________________________________________________________________________

    This prototype creates an mutable dataclass with the fields and methods. It also supports multiple
    environments.

    Application Config Requirements:

        1) support multiple environments (devop, test, staging, prod)
        2) mutable and immutable instances
        3) versioned
        4) dot-friendly
        5) support methods that pull config settings from secret locations (apikeys, db passwords, etc)

    Config Alternatives:

        1) config parser - file-based config; error prone and not type-safe
        2) type dictionary - typed good, mutable bad
        3) custom classes - ok, but namedtuple is an easier way 
        4) dataclass - mutable

    dpw | 2023.08.19
    _____________________________________________________________________________________________________
    """

    print(s)


@dataclass
class AppConfig:
    env: str
    created: str
    name: str
    port: int
    weight: float
    version: str
    apikey: str
    dbpw: str

    def freeze(self) -> namedtuple:
        keys = ' '.join(self.__dict__.keys())
        Frozen = namedtuple('Frozen', keys)
        return Frozen(**self.__dict__)


def create_app_config(env):
    # use env var to point to the correct env...

    apikey = f"{env}-*******"
    dbpw = f"{env}-*******"

    now = time.gmtime()
    ts = time.strftime("%Y-%m-%dT%H:%M:%S.%s", now)

    return AppConfig(
        env=env,
        created=ts,
        name="cfg",
        port=5050,
        weight=3.44,
        version="0.1.0",
        apikey=apikey,
        dbpw=dbpw
    )



if __name__ == "__main__":
    args = sys.argv[1:]
    notes()

    cfg = create_app_config("dev")
    print(f"config:  {cfg}")

    print(f"name: {cfg.name}")

    conf = cfg.freeze()

    print(conf)

    # this will throw
    # cfg.env = "prod"
    # print(cfg, cfg.env)
