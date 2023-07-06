#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-05 18:55:20

import begin
import math.sin
import math.cos

def afn(x,y): return cos(y)
def bfn(x,y): return x / (y - 1)
def cfn(x,y): return x / (y + 1)
def dfn(x,y): return (x - 1) / y
def efn(x,y): return (x + 1) / y

def test(x, y):
    print(f'point ({x},{y})')
    fn_list = [afn, bfn, cfn, dfn, efn]
    for fn in fn_list:
        print(f'{fn.__name__}({x},{y}) = {fn(x,y) }')


@begin.start
def main(arg1 = None):
    x, y = 5, -7
    test(x, y)

