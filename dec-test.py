#!/usr/bin/env python3

from decimal import *

ctx = getcontext()

num1 = Decimal('1.1')
num2 = Decimal('1.563')
num3 = num1 + num2

print(num3)
print(num1 ** 4)
ctx.prec = 4
print(num1 ** 4)
