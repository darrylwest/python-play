#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-31 16:27:12

import sys
from rich import inspect

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(metaclass=Singleton):
    pass

def main(args: list) -> None:
    x = MyClass()
    y = MyClass()

    assert x is y

    inspect(x)
    inspect(y)

if __name__ == '__main__':
    main(sys.argv[1:])

