#!/usr/bin/env python3
# dpw@plaza.local
# 2023-12-01 01:23:11

import sys
from rich import print
import random

def main(args: list) -> None:
    # print(f'{args}')
    otp = ''.join(random.choices('0123456789', k=6))
    print(otp)

if __name__ == '__main__':
    main(sys.argv[1:])

