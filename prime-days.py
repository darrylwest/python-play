#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-21 23:44:42
#
import sympy as sym
import datetime
from datetime import timedelta

start_year = 2023
start_date = datetime.date(start_year, 1, 1)
count = 365


def is_prime(n):
    p = sym.factorint(n)

    return len(p) == 1


for idx in range(0, count):
    delta = timedelta(days=idx)
    dt = start_date + delta
    n = int("{}{:02d}{:02d}".format(dt.year, dt.month, dt.day))

    print(n, is_prime(n))
