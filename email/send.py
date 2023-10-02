#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-02 17:49:39

import sys
from rich import print
import smtplib, ssl
import tomllib
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

@dataclass
class Config:
    host: str
    user: str
    pw: str

    @classmethod
    def from_dict(cls, cfg: dict):
        return cls(
            host=f'smtp{cfg.get("EMAIL_HOST")}',
            user=cfg.get("EMAIL_USER"),
            pw=cfg.get("EMAIL_PW"),
        )

def read_config(filename: str):
    path = Path(filename)
    data = tomllib.loads(path.read_text())

    return data

def send(ctx: Config, email_to: str, message: str):
    port = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(ctx.host, port, context=context) as server:
        server.login(ctx.user, ctx.pw)
        resp = server.sendmail(ctx.user, email_to, message)


def main(args: list) -> None:
    # print(f'{args}')
    username = 'dpw500'
    subject = 'message sender...'
    body = f'message sent at {datetime.utcnow()}'
    email_to = '1426charlie@gmail.com'

    cfg = read_config("email/config.toml")
    config = Config.from_dict(cfg.get(username))

    message = f'From: {config.user}\nTo: {email_to}\nSubject: {subject}\n\n{body}'
    print(message)

    send(config, '1426charlie@gmail.com', message)

    

if __name__ == '__main__':
    main(sys.argv[1:])

