#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-20 15:28:01

import sys
import time
from rich import print
import pickle
from pathlib import Path

from rpc.command import Command

def encode(obj, filename: Path):
    with open(filename, 'wb') as writer:
        pickle.dump(obj, writer)

def decode(filename: Path):
    with open(filename, 'rb') as reader:
        obj = pickle.load(reader)

    return obj

def main(args: list) -> None:
    cmd = Command('my-rpc-command', time.time_ns)

    print(cmd)




if __name__ == '__main__':
    main(sys.argv[1:])

