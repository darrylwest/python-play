#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-31 16:29:09

import sys
from rich import inspect

"""
Creates a singleton through a factory method.  Can be useful to enable testing, but,
it's possible to create multiple instances. (user beware).
"""

class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        """Static access method."""
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """Virtually private constructor."""
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


def main(args: list) -> None:
    print(f"{args}")
    x = Singleton.get_instance()
    y = Singleton.get_instance()

    assert x is y

    inspect(x)
    inspect(y)


if __name__ == "__main__":
    main(sys.argv[1:])
