#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-18 19:04:03

import datetime
import multiprocessing
import os
import time


def func(x):
    start = datetime.datetime.now()
    time.sleep(0.01)
    end = datetime.datetime.now()

    return f"pid: {os.getpid()} x={x} start at {start}, end at {end}"


if __name__ == "__main__":
    print(f"running with a pool ops...")
    data = list(range(1, 100))
    with multiprocessing.Pool() as pool:
        data = pool.map(func, data)

    for row in data:
        print(row)
