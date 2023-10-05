#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-07 17:09:08

import math
import random


def calc_phi():
    # the random start value
    phi = (1 + math.sqrt(5)) / 2
    x = random.uniform(-10.0, 10.0)
    print(f"start number = {x}")

    count = 50
    for n in range(count):
        x = 1 + 1.0 / x

    print(f"Phi calculation result: {x} after {count} rounds, error: {phi - x}...")


if __name__ == "__main__":
    calc_phi()
