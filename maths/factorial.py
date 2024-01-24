#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2024-01-24 17:12:55

import sys
from rich import print

def main(args: list) -> None:
    n = 4
    fact = 1
     
    for i in range(1, n+1):
        fact = fact * i
     
    print("The factorial of 23 is : ", end="")
    print(fact)

if __name__ == '__main__':
    main(sys.argv[1:])

