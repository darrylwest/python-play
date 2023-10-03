#!/usr/bin/env python3
# dpw@piedmont
# 2023-08-22 13:23:12

import sys

from rich import print


def application(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"hello world"]


def main(args: list) -> None:
    print(f"{args}")
    print(
        "start service with this: uwsgi --http :9090 --wsgi-file web/wsgi-app.py  --master --processes 4 --threads 2"
    )


if __name__ == "__main__":
    main(sys.argv[1:])
