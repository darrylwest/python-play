#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-03 19:45:41

import random
import sys

from rich import print
from twilio.rest import Client


def send_sms(send_to: str, msg):
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    message = client.messages.create(from_="", body=msg, to=send_to)

    print(message.sid)


def main(args: list) -> None:
    # print(f'{args}')
    otp = random.randint(100000, 999999)
    msg = f"otp: {otp}"

    phone = "+17752508168"
    send_sms(phone, msg)


if __name__ == "__main__":
    main(sys.argv[1:])
