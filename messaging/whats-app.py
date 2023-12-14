#!/usr/bin/env python3
# dpw@tiburon.local
# 2023-12-13 20:17:20

'''
This is kind of clunky because it requires you have a registered device and that it's open for it to work.
But, it does get the message to the browser, then you have to press send.
'''

import sys
from rich import print
from datetime import datetime
import pywhatkit as kit

def send(args):
    now = datetime.today().isoformat()
    print(f'now = {now}')
    msg = f'{args[0]} at {now}'
    kit.sendwhatmsg_instantly("+17752508168", msg)

def main(args: list) -> None:
    print(f'{args}')
    send(args)

if __name__ == '__main__':
    main(sys.argv[1:])

