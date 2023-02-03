#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-03 21:03:03
#

from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


x = [0, 1, 2]
y = [1, 3, 2]

f = interp1d(x, y)
y_hat = f(1.75)
print(y_hat)

plt.figure(figsize = (10,8))
plt.plot(x, y, '-ob')
plt.plot(1.75, y_hat, 'ro')
plt.title('Linear Interpolation at x = 1.75')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

