#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-01 18:41:17

import sys
import os
from rich import print
import imaplib

def read_all():
    mb = imaplib.IMAP4_SSL(os.getenv('EMAIL_HOST'))
    mb.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PW'))
    mb.select()
    typ, data = mb.search(None, 'ALL')

    print(f'Type: {typ}')
    print(f'Data: {data}')

    for num in data[0].split():
        typ, data = mb.fetch(num, '(RFC822)')
        print(f'Msg: {num.decode()}')
        lines = data[0][1].split()
        for line in lines:
            print(line)

    mb.close()
    mb.logout()

def main(args: list) -> None:
    # print(f'{args}')
    read_all()

if __name__ == '__main__':
    main(sys.argv[1:])

