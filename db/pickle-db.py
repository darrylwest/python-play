#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-05 18:49:39

import sys
from rich import print
import pickledb

def main(args: list) -> None:
    print(f'{args}')
    db = pickledb.load('data/pickledb.json', False)
    db.set('my-key', 'my-value')

    print(db.get('my-key'))
    db.dump()

if __name__ == '__main__':
    main(sys.argv[1:])

