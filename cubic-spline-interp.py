#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-03 21:08:32
#

from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt


x = [0, 1, 2]
y = [1, 3, 2]

# use bc_type = 'natural' adds the constraints as we described above
f = CubicSpline(x, y, bc_type='natural')
x_new = np.linspace(-10, 6, 500)
y_new = f(x_new)

plt.figure(figsize = (10,8))
plt.plot(x_new, y_new, 'b')
plt.plot(x, y, 'ro')
plt.title('Cubic Spline Interpolation',fontweight='bold')
plt.xlabel('x')
plt.ylabel('y')

plt.xlim([-3,5])
plt.ylim([-2,8])

plt.plot([-13,14],[0,0],color='gray')
plt.plot([0,0],[-500,1200],color='gray')

plt.grid()
plt.show()

