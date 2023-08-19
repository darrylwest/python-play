#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-28 16:18:41

import time
from collections import namedtuple


def notes():
    s = """
    _____________________________________________________________________________________________________

    This prototype creates an immutable namedtuple with the fields and methods. Is supports multiple
    environments.

    Application Config Requirements:

        1) support multiple environments (devop, test, staging, prod)
        2) immutable
        3) versioned
        4) dot-friendly
        5) support methods that pull config settings from secret locations (apikeys, db passwords, etc)

    Config Alternatives:

        1) config parser - file-based config; error prone and not type-safe
        2) type dictionary - typed good, mutable bad
        3) custom classes - ok, but namedtuple is an easier way 
        4) dataclass - mutable

    dpw | 28-Jul-2023
    _____________________________________________________________________________________________________
    """

    print(s)


AppConfig = namedtuple("AppConfig", "env created name port weight version apikey dbpw")



# this should probably be wrapped in a 'secrets' class to enable more logic
# pull from secrets based on env
def apikey(env):
    return f"{env}-*******"


# pull from secrets based on env
def dbpw(env):
    return f"{env}-*******"


def create_app_config(env):
    # use env var to point to the correct env...
    now = time.time_ns()

    def apikey_fn():
        return apikey(env)

    def dbpw_fn():
        return dbpw(env)

    return AppConfig(
        env,
        now,
        "AppConfig",
        4040,
        34.22,
        "1.0.5",
        apikey_fn,
        dbpw_fn,
    )


@begin.start
def main(arg1=None):
    notes()

    cfg = create_app_config("develop")
    print(f"config:  {cfg}")

    print(f"name: {cfg.name}, apikey: {cfg.apikey()}, dbpw: {cfg.dbpw()}")

    # this will throw
    # cfg.env = "prod"
    # print(cfg, cfg.env)
