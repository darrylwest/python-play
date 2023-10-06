#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-02 17:49:39

import random
import smtplib
import sys
import tomllib
from dataclasses import dataclass
from datetime import datetime, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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
    # email_to = "1426charlie@gmail.com"
    # email_to = "7752508168@messaging.sprintpcs.com"
    email_to = "dpw@raincitysoftware.com"

    msg = MIMEMultipart()
    msg["From"] = username
    msg["To"] = email_to
    msg["Subject"] = "otp..."

    key = random.randint(100000, 999999)
    body = f"OTP: {key} generated {datetime.now(tz=timezone.utc)}."

    msg.attach(MIMEText(body, "plain"))

    cfg = read_config("email/config.toml")
    config = Config.from_dict(cfg.get(username))

    send(config, email_to, msg.as_string())

    print(f"sent message to {email_to}: {body}")


if __name__ == "__main__":
    main(sys.argv[1:])
