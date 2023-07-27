#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-27 13:40:12

import begin
from collections import defaultdict

def add_dogs(dd):
    dd['dogs'].append('Fido')
    dd['dogs'].append('HotDog')
    dd['dogs'].append('Lassy')

def add_cats(dd):
    dd['cats'].append('Boxcar')
    dd['cats'].append('Fluffy')
    dd['cats'].append('Whiskers')

@begin.start
def main(arg1 = None):
    print('creates a short lists of dogs and cats')
    dd = defaultdict(list)

    add_dogs(dd)
    add_cats(dd)

    print(dd)
    print(f'length: {len(dd)}')

