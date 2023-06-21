#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-21 20:28:42

import asyncio
import tornado

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello tornado")

def make_app():
    return tornado.web.Application([ (r"/", Handler), ])

async def main():
    port = 8888
    app = make_app()
    print(f'listen on port {port}')
    app.listen(port)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())

