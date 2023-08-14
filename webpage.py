#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-21 13:48:06

import begin
import pyvibe as pv


def create_page():
    page = pv.Page("Vibe Generated")
    page.add_header("My Web Page")
    page.add_text("This is my first home page.")

    with page.add_card() as card:
        card.add_header("My Special Notice Card")
        card.add_text("This is the body text of the notice.")
        card.add_link(
            "More to learn here", "https://www.pyvibe.com/component_reference.html"
        )

    print(page.to_html())


@begin.start
def main(arg1=None):
    create_page()
