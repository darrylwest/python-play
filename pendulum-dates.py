#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-06 19:58:19

import begin
import pendulum

def show():
    dt = pendulum.datetime(2023, 1, 31)
    print(f' dt: {dt}')

    for n in range(0,20):
        utc = pendulum.now('UTC')
        print(f'utc: {utc}')

@begin.start
def main(arg1 = None):
    show()
