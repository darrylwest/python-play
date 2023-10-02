#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-01 18:41:17

import email
import imaplib
import os
import sys
import tomllib
from dataclasses import dataclass
from datetime import datetime
from email.header import decode_header
from pathlib import Path

from rich import inspect, print


@dataclass
class Config:
    host: str
    user: str
    pw: str
    folder: str
    search: str

    @classmethod
    def from_dict(cls, cfg: dict):
        return cls(
            host=f'imap{cfg.get("EMAIL_HOST")}',
            user=cfg.get("EMAIL_USER"),
            pw=cfg.get("EMAIL_PW"),
            folder=cfg.get("FOLDER", "INBOX"),
            search=cfg.get("SEARCH", "UNSEEN"),
        )


@dataclass
class EmailResponse:
    ts: datetime
    send_by: str
    sent_at: str
    subject: str
    body: str


def read_config(filename: str):
    path = Path(filename)
    data = tomllib.loads(path.read_text())

    return data


def read_all(ctx: Config) -> list[EmailResponse]:
    mb = imaplib.IMAP4_SSL(ctx.host)
    mb.login(ctx.user, ctx.pw)
    # typ, data = mb.search(None, 'UNSEEN')
    mb.select(ctx.folder)
    typ, data = mb.search(None, ctx.search)

    emails = []

    for num in data[0].split():
        typ, data = mb.fetch(num, "(RFC822)")
        for resp_part in data:
            if isinstance(resp_part, tuple):
                msg = email.message_from_bytes(resp_part[1])

                # print(msg)

                # resp = EmailResponse()
                mfrom = msg["from"]
                subject = msg["subject"]
                dt = msg["date"]

                # TODO(dpw): create a rich table...
                print(f"From: {mfrom}")
                print(f"Sent: {dt}")
                print(f"Subj: [green3]{subject}")

                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.as_string().split("\n")
                        text = "".join([f"{tx}\n" for tx in body[1:] if tx != ""])
                        print(f"Body: [green3]{text}")

    mb.close()
    mb.logout()

    return emails


def main(args: list) -> None:
    # print(f'{args}')
    cfg = read_config("email/config.toml")
    dpw500 = Config.from_dict(cfg.get("dpw500"))
    dpw = Config.from_dict(cfg.get("dpw"))

    if "--all" in args:
        dpw500.search = "ALL"
        dpw.search = "ALL"

    if "--verbose" in args:
        print(dpw500)
        print(dpw)

    read_all(dpw500)
    read_all(dpw)


if __name__ == "__main__":
    main(sys.argv[1:])
