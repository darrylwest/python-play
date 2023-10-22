#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-21 13:33:16

import math
import random
import time

from mpire import WorkerPool
from rich import inspect


def calc_pi(x: int):
    samples = 1000000

    circle_points = 0
    square_points = 0
    # Total Random numbers generated= possible x
    # values* possible y values

    for _ in range(samples):
        # Randomly generated x and y values from a
        # uniform distribution
        # Range of x and y values is -1 to 1
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)

        origin_dist = rand_x**2 + rand_y**2

        # Distance between (x, y) from the origin

        # Checking if (x, y) lies inside the circle
        if origin_dist <= 1:
            circle_points += 1

        square_points += 1

        # Estimating value of pi,
        # pi= 4*(no. of points generated inside the
        # circle)/ (no. of points generated inside the square)
        pi = 4 * circle_points / square_points

    # print(rand_x, rand_y, circle_points, square_points, "-", pi)
    # print("\n")

    return pi


if __name__ == "__main__":
    t0 = time.perf_counter()
    with WorkerPool(n_jobs=10) as pool:
        results = pool.map(calc_pi, range(20), progress_bar=True)

    t1 = time.perf_counter()
    print(results)
    estimate = sum(results) / len(results)

    print(f"estimate: {estimate}, actual: {math.pi}, error: {math.pi - estimate}")

    print(f"duration: {t1 - t0}")
