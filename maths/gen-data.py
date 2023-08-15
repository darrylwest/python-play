#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-11 17:58:06
#

import numpy as np

# matrix = np.zeros


def gen_xy():
    for y in range(-10, 10):
        for x in range(-10, 10):
            print(x, y)


def gen_xyz():
    for z in range(-10, 10):
        for y in range(-10, 10):
            for x in range(-10, 10):
                print(x, y, z)


# gen_xyz()
gen_xy()
