#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-26 15:13:54

from gmail.gmail import gmail

# need to create a google app-passkey to use this


def send_gmail(subject, body, to):
    email = gmail()
    # email_id =
    # email_pw =
    email.login(email_id, email_pw)
    email.receiver_mail(to)
    email.send_mail(subject, body)
    print(f"message {subject} sent to: {to}")


if __name__ == "__main__":
    # read the id and pw from local store...
    print("not ready yet...")

    # send_gmail("my test message", "this is test message # 1...", "darryl.west@raincitysoftware.com")
