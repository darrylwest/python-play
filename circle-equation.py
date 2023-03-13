#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-13 17:39:29
#

import argparse
import numpy as np
from numpy.lib.scimath import sqrt
import matplotlib.pyplot as plt
from collections import namedtuple

parser = argparse.ArgumentParser(description='Enter the circle center and radius as x y r')
parser.add_argument('numbers', metavar='3', type=float, nargs='+', help='the circle center x,y and radius r')

args = parser.parse_args()

figure, axes = plt.subplots()
cx = args.numbers[0]
cy = args.numbers[1]
radius = args.numbers[2]

angle = np.linspace(0, 2*np.pi, 360)

x = radius * np.cos(angle) + cx
y = radius * np.sin(angle) + cy

axes.plot(x, y)
axes.set_aspect( 1 )

plt.title('Circle')
plt.grid()
plt.show()
