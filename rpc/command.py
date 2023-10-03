#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-19 21:36:41

import pickle
import sys
import time
from pathlib import Path

from rich import print


class RPCBase:
    def save(obj):
        """Added this to help pickle save the obj"""
        return (obj.__class__, obj.__dict__)

    def restore(cls, attrs):
        """Added this to help pickle re-instate the obj"""
        obj = cls.__new__(cls)
        obj.__dict__.update(attrs)
        return obj

    def to_string(obj):
        """pickle the object then base64 encode and return the string"""
        pass

    def encode(obj, filename: Path) -> None:
        """encode with pickle to the file"""
        with open(filename, "wb") as writer:
            pickle.dump(obj, writer)

    def decode(filename: Path):
        """decode the file with pickle and return the obj"""
        with open(filename, "rb") as reader:
            obj = pickle.load(reader)

        return obj


class Command(RPCBase):
    def __init__(self, name: str, timestamp: int):
        self.name = name
        self.timestamp = timestamp

    def __repr__(self):
        return f"{self.__class__.__name__}({vars(self)})"

    def show(self):
        print(f"{self.name=}, ts: {self.timestamp()}")


def main(args: list) -> None:
    cmd = Command("rpc", time.time_ns)

    print(cmd)
    cmd.show()

    path = Path("/tmp/cmd.pkl")

    print(f"save cmd to {path}")
    RPCBase.encode(cmd, path)

    print(f"read and decode from {path}")
    c1 = RPCBase.decode(path)

    print(c1)

    # data = {mything:'this is a test'}
    # b64 =


if __name__ == "__main__":
    main(sys.argv[1:])
