#!/usr/bin/env python3
# dpw@tiburon.local
# 2023-12-09 17:46:58

import sys
from rich import print
from googlesearch import search

def main(args: list) -> None:
    print(f'search for {args}')

    query = "issaquah"

    for url in search(query):
        print(url)

if __name__ == '__main__':
    main(sys.argv[1:])

