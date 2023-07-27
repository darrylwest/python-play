#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-27 14:05:02

import begin
from collections import deque

def create_stack():
    stack = deque()

    stack.append('eat')
    stack.append('code')
    stack.append('sleep')

    return stack

@begin.start
def main(arg1 = None):
    stack = create_stack()

    print(f'stack: {stack}')

    print(f'1 pop() {stack.pop()}')
    print(f'2 pop() {stack.pop()}')
    print(f'3 pop() {stack.pop()}')
