#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-27 14:05:02

from collections import deque


def create_stack():
    stack = deque()

    stack.append("eat")
    stack.append("code")
    stack.append("sleep")

    return stack


if __name__ == "__main__":
    stack = create_stack()

    print(f"stack: {stack}")

    print(f"1 pop() {stack.pop()}")
    print(f"2 pop() {stack.pop()}")
    print(f"3 pop() {stack.pop()}")
