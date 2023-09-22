#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-22 18:31:29

import sys
# from rich import print
import itertools
from threading import Thread, Event
import time

def spin(msg: str, done: Event) -> None:

    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break

    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='', flush=True)

def slow() -> int:
    time.sleep(3)
    return 42

def supervisor() -> int:
    done = Event()
    msg = 'working!'
    spinner = Thread(target=spin, args=(msg, done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    print(f'\rdone {msg}', flush=True)

    return result

def main(args: list) -> None:
    result = supervisor()
    print(f'result: {result}')

if __name__ == '__main__':
    main(sys.argv[1:])

