#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-27 14:20:27

# NOTE: see concurrency/async-queue.py to get

from collections import deque


# creates a FIFO queue
def create_queue():
    q = deque()

    q.append("1 eat")
    q.append("2 code")
    q.append("3 sleep")

    return q


if __name__ == "__main__":
    fifo = create_queue()

    print(f"queue {fifo} (non-blocking)")

    print(f"1 pop left: {fifo.popleft()}")
    print(f"2 pop left: {fifo.popleft()}")
    print(f"3 pop left: {fifo.popleft()}")
