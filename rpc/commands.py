#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-19 21:36:41

import sys
import time

class Commands:
    def __init__(self, name: str, timestamp: int):
        self.name = name
        self.timestamp = timestamp

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__dict__.copy()})'

    def __str__(self):
        return f'{self.__class__.__name__}({vars(self)})'

    def show(self):
        print(f'{self.name=}, {self.timestamp=}')

    def save(obj):
        """Added this to help pickle save the obj"""
        return (obj.__class__, obj.__dict__)

    def restore(cls, attrs):
        """Added this to help pickle re-instate the obj"""
        obj = cls.__new__(cls)
        obj.__dict__.update(attrs)
        return obj

def main(args: list) -> None:
    cmds = Commands("rpc", time.time_ns())

    print(cmds)
    cmds.show()

if __name__ == '__main__':
    main(sys.argv[1:])

