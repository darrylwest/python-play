#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-02 17:49:39

import random
import smtplib
import sys
import tomllib
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from rich import print


@dataclass
class Config:
    host: str
    user: str
    pw: str

    @classmethod
    def from_dict(cls, cfg: dict):
        return cls(
            host=f'smtp{cfg.get("email_host")}',
            user=cfg.get("email_user"),
            pw=cfg.get("email_pw"),
        )


def read_config(filename: str):
    path = Path(filename)
    data = tomllib.loads(path.read_text())

    return data


def send(ctx: Config, email_to: str, message: str):
    port = 465

    with smtplib.SMTP_SSL(ctx.host, port) as server:
        server.login(ctx.user, ctx.pw)
        resp = server.sendmail(ctx.user, email_to, message)


def main(args: list) -> None:
    # print(f'{args}')
    username = "dpw500"
    key = random.randint(100000, 999999)
    subject = f"otp:"
    body = f"{key} at {datetime.now(tz=timezone.utc)}"

    # email_to = "1426charlie@gmail.com"
    email_to = "7752508168@messaging.sprintpcs.com"
    # email_to = 'dpw@raincitysoftware.com'

    cfg = read_config("email/config.toml")
    config = Config.from_dict(cfg.get(username))

    message = f"From: {config.user}\nTo: {email_to}\nSubject: {subject}\n\n{body}"

    print(message)

    send(config, email_to, message)


if __name__ == "__main__":
    main(sys.argv[1:])
