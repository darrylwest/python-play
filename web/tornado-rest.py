#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-21 22:59:00

import asyncio
import sys

import tornado
from rich import inspect, print


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello, world")


class LoggerHandler(tornado.web.RequestHandler):
    def get(self):
        inspect(self)
        self.write("you should post to this")


def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/v1/logit/appname", LoggerHandler),
        ]
    )


async def main(args: list) -> None:
    port = 8888
    print(f"listening on port: {port}, {args}")
    app = make_app()
    app.listen(port)
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))
