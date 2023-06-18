#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-18 19:31:59


import begin

@begin.start
def main(name='Arther', quest='Holy Grail', color='blue', *knights):
    print(f'hello {name} {quest} {color} {knights}')

