#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-24 18:36:19

import time


def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print("Generates an infinite fib sequence...")
    fgen = fib_generator()
    while True:
        print(next(fgen))
        time.sleep(0.2)
