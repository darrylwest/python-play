#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-19 17:53:39
#

# use Quadratic Equation to solve ax2 + bx + c; print and save a graph of the equation

import argparse
import scipy as sp
import sympy as sym
import numpy as np
from numpy.lib.scimath import sqrt
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Enter three coefficient values to calculate the quadratic roots')
parser.add_argument('numbers', metavar='N', type=float, nargs='+', help='the coefficients a, b, and c') 
args = parser.parse_args()

def plotit(a, b, c):
    # x = sym.symbols('x')
    x = np.linspace(-12, 12, 1000)
    y = a*x**2 + b*x + c
    plt.plot(x, y)
    plt.grid()
    return plt


if len(args.numbers) != 3:
    print("Error: please supply values for a, b and c, e.g., 2 7 5")
else:
    a = args.numbers[0]
    b = args.numbers[1]
    c = args.numbers[2]
    quadp = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    quadn = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

    print('Solution for ', args.numbers, 'is:', quadp, ',', quadn)
    plt = plotit(a, b, c)
    title = ' '.join(['Solution',str(a),str(b),str(c),'=',str(quadp),',',str(quadn)])
    plt.suptitle("x = (-b ± √b^2 - 4ac) / 2*a",fontsize='large',fontweight='bold')
    plt.title(title,fontsize='large',fontweight='bold')
    fname = '/tmp/plot.pdf'
    plt.savefig(fname)
    print(f"Plot written to {fname}.")
    # plt.show()

