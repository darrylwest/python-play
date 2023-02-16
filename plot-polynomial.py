#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-16 20:52:16
#

# import matplotlib
# matplotlib.use("SVG")

import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return (x + 3)*(x - 2)*(x + 1)

plt.ylabel('y-axis')
plt.xlabel('y = (x + 3)*(x - 2)*(x + 1)')
plt.title('graph of y = x^3 + 2x^2 - 5x - 6')


x = np.linspace(-3.4, 2.4, 500)
y = f(x)

plt.plot(x, y)
plt.grid()

x = [-3, -1, 0, 2]
y = [0, 0, -6, 0]
plt.plot(x, y, 'ro')

plt.plot([-4,3],[0,0],color='gray')
plt.plot([0,0],[9,-9],color='gray')

# fig = plt.figure(figsize=(3.0, 3.0))

filename = 'poly.png'
plt.savefig(filename)

# plt.show()

print("see file: ", filename)

