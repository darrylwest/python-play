#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-03 19:45:41

import sys
from rich import print
from twilio.rest import Client
import random


def send_sms(send_to: str, msg):

    account_sid = 'ACe5a0ace9f7acc9303fbf4b8f9b01fa0f'
    auth_token = '315305d5265ac8ded26afd06e39392b7'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
      from_='+18555996772',
      body = msg,
      to=send_to
    )

    print(message.sid)

def main(args: list) -> None:
    # print(f'{args}')
    otp = random.randint(100000, 999999)
    msg = f'otp: {otp}'

    phone = '+17752508168'
    send_sms(phone, msg)

if __name__ == '__main__':
    main(sys.argv[1:])

