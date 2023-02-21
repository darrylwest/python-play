#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-21 22:13:00
#

import numpy as np
import matplotlib.pyplot as plt

plt.ylabel('y-axis')
plt.xlabel('roots [-12,3,12], [-6,8]')
plt.suptitle('Cubic & Derivatives',fontsize=14,fontweight='bold',y=0.99)
plt.title('f(x) = x^3 - 3x^2 - 144x - 432',fontsize=12)

plt.xlim([-13,13])
plt.ylim([-500,1000])

x = np.linspace(-13, 14, 1000)
y = x**3 - 3*x**2 - 144*x + 432
plt.plot(x, y, label='cubic')

y = 3*x**2 - 6*x - 144
plt.plot(x, y, label='1st der')

y = 6*x - 6
plt.plot(x, y, label='2nd der')

y = -147*x + 433
plt.plot(x, y, label='tangent')

plt.legend()
plt.grid()

plt.show()
