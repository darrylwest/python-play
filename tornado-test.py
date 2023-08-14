#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-21 20:28:42

#
# TODO: add tornado.httpclient for client tests with AsyncHTTPClient
#

import asyncio
import tornado
import pyvibe as pv


def home_page():
    page = pv.Page("Vibe Generated")
    page.add_header("My Web Page")
    page.add_text("This is my first home page.")

    with page.add_card() as card:
        card.add_header("My Special Notice Card")
        card.add_text("This is the body text of the notice.")
        card.add_link(
            "More to learn here", "https://www.pyvibe.com/component_reference.html"
        )

    return page.to_html()


class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write(home_page())


def make_app():
    return tornado.web.Application(
        [
            (r"/", Handler),
        ]
    )


async def main():
    port = 8888
    app = make_app()
    print(f"listen on port {port}")
    app.listen(port)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
