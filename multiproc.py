#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-18 19:04:03

import multiprocessing
import time
import datetime


def func(x):
    start = datetime.datetime.now()
    time.sleep(1)
    end = datetime.datetime.now()

    return f"x={x} start at {start}, end at {end}"


if __name__ == "__main__":
    n = 3
    print(f"running with a pool of {n} processes and requestion 7 ops...")
    with multiprocessing.Pool(processes=n) as pool:
        data = pool.map(func, [1, 2, 3, 4, 5, 6, 7])

    for row in data:
        print(row)
