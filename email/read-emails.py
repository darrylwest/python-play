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

import rich
from rich.console import Console
from rich.table import Table

VERSION = "0.1.1"

console = Console()


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
            host=f'imap{cfg.get("email_host")}',
            user=cfg.get("email_user"),
            pw=cfg.get("email_pw"),
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
        if isinstance(self.sent_at, str):
            ts = float(self.sent_at) / 1_000

            sent_at = datetime.fromtimestamp(ts).isoformat()
        else:
            sent_at = ""

        table = Table(
            "To", self.sent_to, "From", self.sent_from, box=rich.box.SIMPLE_HEAVY
        )
        table.add_row("Date", f'[cyan]{sent_at}', "Subject", f"[green3]{self.subject}")

        console.print(table)
        # console.print(Table(self.body, box=rich.box.SIMPLE))


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
                    # sent_to=ctx.user,
                    sent_to=msg.get('X-Original-To'),
                    sent_from=msg.get('Return-Path'),
                    sent_at=msg.get("X-MC-Ingress-Time"),
                    subject=msg.get("Subject"),
                )

                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.as_string().split("\n")
                        text = "".join([f"{tx}\n" for tx in body[1:] if tx != ""])
                        # resp.body = text

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
        print(f"{sys.argv[0]}, Version: {VERSION}")

    if "--verbose" in args:
        dpw500.verbose = True
        dpw.verbose = True

    emails = read_all(dpw500)
    emails = read_all(dpw)


if __name__ == "__main__":
    main(sys.argv[1:])
