#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-11 16:17:04
#


import numpy as np

start = -10
stop = 10
count = stop - start + 1

x = np.linspace(start, stop, count)
y = np.linspace(start + 1, stop + 1, count)
z = np.linspace(start + 2, stop + 2, count)

matrix = np.array([x, y, z])
matrix = matrix.T

def iterate_matrix(matrix):
    for i in range(matrix.shape[0]):
        row = matrix[i, :]
        print("row ", i+1, ":", row)


iterate_matrix(matrix)

