#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-01 18:41:17

import sys
import os
from rich import print, inspect
import imaplib
import email

def read_all():
    mb = imaplib.IMAP4_SSL(os.getenv('EMAIL_HOST'))
    mb.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PW'))
    # typ, data = mb.search(None, 'UNSEEN')
    mb.select('inbox')
    typ, data = mb.search(None, 'ALL')

    # typ, data = mb.search(None, 'UNSEEN')
    # print(f'Type: {typ}')

    for num in data[0].split():
        typ, data = mb.fetch(num, '(RFC822)')
        for resp_part in data:
            if isinstance(resp_part, tuple):
                msg = email.message_from_bytes(resp_part[1])
                mfrom = msg['from']
                subject = msg['subject']
                dt = msg['date']

                # TODO(dpw): create a rich table...
                print(f'From: {mfrom}')
                print(f'Sent: {dt}')
                print(f'Subj: [green3]{subject}')

                for part in msg.walk():
                    if part.get_content_type() == 'text/plain':
                        body = part.as_string().split('\n')
                        text = ''.join([f'{tx}\n' for tx in body[1:] if tx != ''])
                        print(f'Body: [green3]{text}')


    mb.close()
    mb.logout()

def main(args: list) -> None:
    # print(f'{args}')
    read_all()

if __name__ == '__main__':
    main(sys.argv[1:])

