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

VERSION = "0.1.0"

@dataclass
class Config:
    host: str
    user: str
    pw: str
    folder: str
    search: str
    verbose: bool = False

    @classmethod
    def from_dict(cls, cfg: dict):
        return cls(
            host=f'imap{cfg.get("EMAIL_HOST")}',
            user=cfg.get("EMAIL_USER"),
            pw=cfg.get("EMAIL_PW"),
            folder=cfg.get("FOLDER", "INBOX"),
            search=cfg.get("SEARCH", "ALL"),
        )


@dataclass
class EmailResponse:
    mid: str
    sent_to: str
    sent_from: str
    sent_at: str
    subject: str
    body: str = ""

    def show(self):
        # TODO(dpw): create a rich table...
        print(f"ID  : {self.mid}")
        print(f"To  : {self.sent_to}")
        print(f"From: {self.sent_from}")
        print(f"Sent: {self.sent_at}")
        print(f"Subj: [green3]{self.subject}")
        print(f"Body: [green3]{self.body}")


def read_config(filename: str):
    path = Path(filename)
    data = tomllib.loads(path.read_text())

    return data


def read_all(ctx: Config) -> list[EmailResponse]:
    mb = imaplib.IMAP4_SSL(ctx.host)
    mb.login(ctx.user, ctx.pw)
    mb.select(ctx.folder)
    typ, data = mb.search(None, ctx.search)

    emails = []

    for num in data[0].split():
        _, data = mb.fetch(num, "(RFC822)")
        if ctx.verbose:
            print(data)

        for resp_part in data:
            if isinstance(resp_part, tuple):
                msg = email.message_from_bytes(resp_part[1])

                resp = EmailResponse(
                    mid=msg.get("X-Message-ID"),
                    sent_to=ctx.user,
                    sent_from=msg.get("from"),
                    sent_at=msg.get("date"),
                    subject=msg.get("subject"),
                )

                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.as_string().split("\n")
                        text = "".join([f"{tx}\n" for tx in body[1:] if tx != ""])
                        resp.body = text

                emails.append(resp)
                resp.show()

    mb.close()
    mb.logout()

    return emails


def main(args: list) -> None:
    # print(f'{args}')
    cfg = read_config("email/config.toml")
    dpw500 = Config.from_dict(cfg.get("dpw500"))
    dpw = Config.from_dict(cfg.get("dpw"))

    if "--version" in args:
        print(f'{sys.argv[0]}, Version: {VERSION}')

    if "--verbose" in args:
        dpw500.verbose = True
        dpw.verbose = True

    emails = read_all(dpw500)
    emails = read_all(dpw)


if __name__ == "__main__":
    main(sys.argv[1:])
