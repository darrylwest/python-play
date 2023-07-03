#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-03 01:37:23

import begin
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__}() runtime: {end_time - start_time} seconds')
        return result

    return wrapper

@timer
def myfn():
    time.sleep(2.5)
    return 'hello'

@begin.start
def main(arg1 = None):
    myfn()
