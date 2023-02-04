#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-03 22:03:52
#

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*np.pi, 0.01) 

omega = 100
epsilon = 0.01

y = -np.sin(x) 
y_noise = y + epsilon*omega*np.cos(omega*x)
# y_noise = y + epsilon*np.sin(omega*x)

# Plot solution
plt.figure(figsize = (12, 8))
plt.plot(x, y_noise, 'r-', \
         label = 'Derivative cos(x) + noise')
plt.plot(x, y, 'b-', \
         label = 'Derivative of cos(x)')

plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()

