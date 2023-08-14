#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-03 20:16:45
#

import numpy as np

A = np.array([[4, 3, -5], [-2, -4, 5], [8, 8, 0]])

y = np.array([2, 5, -3])

x = np.linalg.solve(A, y)

print(x)
