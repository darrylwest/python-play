#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-21 13:33:16

import math
import random
import time

from numbba import njit


@njit
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples


if __name__ == "__main__":
    mypi = monte_carlo_pi(100)

    print(f"{mypi=} {math.pi=}")
