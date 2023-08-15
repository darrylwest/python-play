#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-27 14:20:27

from collections import deque

import begin


# creates a FIFO queue
def create_queue():
    q = deque()

    q.append("1 eat")
    q.append("2 code")
    q.append("3 sleep")

    return q


@begin.start
def main(arg1=None):
    fifo = create_queue()

    print(f"queue {fifo} (non-blocking)")

    print(f"1 pop left: {fifo.popleft()}")
    print(f"2 pop left: {fifo.popleft()}")
    print(f"3 pop left: {fifo.popleft()}")
