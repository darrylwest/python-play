#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-04 14:21:05

from rich import inspect
import functools

"""
This example always creates a singleton.
"""

def singleton(cls):
    instances = dict()
    @functools.wraps(cls)
    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton

@singleton
class SomeSingleton():
    def __init__(self):
        print('init')



def main() -> None:
    x = SomeSingleton()
    y = SomeSingleton()

    assert x is y
    inspect(x)
    inspect(y)
    

if __name__ == '__main__':
    main()

