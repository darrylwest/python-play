#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-18 20:34:22

import begin

class Counter:
    def __init__(self, initial_count = 0):
        self.count = initial_count

    def __call__(self):
        self.count += 1
        return self.count

@begin.start
def main():

    count = Counter(100)
    print(count())
    print(count())
    print(count())
    print(count())
