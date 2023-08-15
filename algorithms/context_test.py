#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-11 14:23:35

import time
from contextlib import ContextDecorator


class PrintContext(ContextDecorator):
    """Simple enter/exit print class; @see https://docs.python.org/3/library/contextlib.html#contextlib.chdir"""

    def __enter__(self):
        print(f"{time.time_ns()}: starting...")
        return self

    def __exit__(self, *exc):
        print(f"{time.time_ns()}: exiting...")
        return False


@PrintContext()
def func():
    print(f"{time.time_ns()}: my func middle section")


if __name__ == "__main__":
    func()
