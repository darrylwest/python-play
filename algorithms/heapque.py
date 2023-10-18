#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-18 15:42:03

import sys
from rich import print
import heapq 

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)

    return [heapq.heappop(h) for i in range(len(h))]

def main(args: list) -> None:
    # print(f'{args}')
    it = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print(it)
    srt = heapsort(it)
    print(srt)


if __name__ == '__main__':
    main(sys.argv[1:])

