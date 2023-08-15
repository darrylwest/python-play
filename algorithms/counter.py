#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-18 20:34:22

# this is like a closure, but better.


class Counter:
    def __init__(self, initial_count=0):
        self.count = initial_count

    def __call__(self):
        self.count += 1
        return self.count


if __name__ == "__main__":
    count = Counter(100)
    for n in range(10):
        print(count())
