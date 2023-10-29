#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-26 15:13:54

import base64
import os

from gmail import GMail, Message

# need to create a google app-passkey to use this


def read_creds():
    b64 = os.getenv("EMAIL_CREDS")
    creds = base64.decodebytes(b64.encode())

    id, pw = creds.split(b":")

    return (id.decode(), pw.decode())


def send_gmail(subject, body, to):
    id, pw = read_creds()

    gmail = GMail(id, pw)
    msg = Message(subject, to=to, text=body)
    gmail.send(msg)

    print(f"message {subject} sent to: {to}")


if __name__ == "__main__":
    # read the id and pw from local store...
    # print("not ready yet...")

    send_gmail(
        "my test message", "this is test message # 2...", "dpw500@raincitysoftware.com"
    )
