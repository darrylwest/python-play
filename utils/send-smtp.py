#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-01 18:27:33

import smtplib
import sys
from datetime import datetime
from email.message import EmailMessage

from rich import print


def compose():
    msg = EmailMessage()
    msg.set_content(f"this is my message created at {datetime.now()}.")
    msg["Subject"] = "A simple message..."
    msg["From"] = "dpw@raincitysoftware.com"
    msg["To"] = "dpw500@raincitysoftware.com"

    s = smtplib.SMTP("smtp.dreamhost.com")


def main(args: list) -> None:
    print(f"{args}")


if __name__ == "__main__":
    main(sys.argv[1:])
