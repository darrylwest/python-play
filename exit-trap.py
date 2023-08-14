#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-18 18:02:06

import atexit


@atexit.register
def bye():
    print("exiting this process...")


print("hello...")

for i in range(10):
    print(i)
