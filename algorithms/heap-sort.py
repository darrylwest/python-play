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

def heapsort2(iterable):
    heapq.heapify(iterable)
    return heapq.nsmallest(len(iterable), iterable)

def main(args: list) -> None:
    # print(f'{args}')
    it = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print(f'original: {it}')
    srt = heapsort(it)
    print(f'sorted   :{srt}')

    heapq.heapify(it)
    print(f'heapify  :{it}')

    largest = heapq.nlargest(5, it)
    print(f'nlargest :{largest}')

    smallest = heapq.nsmallest(5, it)
    print(f'nsmallest:{smallest}')

    # restore the original
    it = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    heap = heapsort2(it)
    print(f'sort2    :{heap}')


if __name__ == '__main__':
    main(sys.argv[1:])

