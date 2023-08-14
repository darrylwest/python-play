#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-13 17:39:29
#

import argparse
import numpy as np
from numpy.lib.scimath import sqrt
import matplotlib.pyplot as plt
from collections import namedtuple

parser = argparse.ArgumentParser(
    description="Enter the circle center and radius as x y r"
)
parser.add_argument(
    "numbers",
    metavar="3",
    type=float,
    nargs="+",
    help="the circle center x,y and radius r",
)

args = parser.parse_args()

figure, axes = plt.subplots()

cx = args.numbers[0]
cy = args.numbers[1]
radius = args.numbers[2]

axes.plot(cx, cy, "ro")
axes.plot(
    [cx - (radius * 1.1), cx + (radius * 1.04)], [cy, cy], color="green", linewidth=0.5
)
axes.plot(
    [cx, cx], [cy - (radius * 1.04), cy + (radius * 1.1)], color="green", linewidth=0.5
)

a = np.pi / 6
x = radius * np.cos(a) + cx
y = radius * np.sin(a) + cy
axes.plot(x, y, "ro")
plt.xlabel(f"Point at {x:.3f},{y:.3f}")

plt.plot

theta = np.linspace(0, 2 * np.pi, 360)

x = radius * np.cos(theta) + cx
y = radius * np.sin(theta) + cy

axes.plot(x, y)
axes.set_aspect(1)

plt.title(f"Circle at ({cx},{cy}), r={radius}")
# plt.legend()
plt.grid()
plt.savefig("circle.pdf")
