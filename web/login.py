#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-31 16:20:54

import pyvibe as pv


def create_page():
    page = pv.Page("My Login Page")
    # page.add_header(text = 'Here is a regular header')
    page.navbar = pv.Navbar(
        title="my custom nav bar",
        logo="https://raincitysoftware.com/assets/img/autumn-leafs.jpg",
    )
    page.footer = pv.Footer(title="___my custom footer___")

    with page.add_card() as card:
        card.add_header("Please Sign In")
        with card.add_form() as form:
            form.add_formtext("Name", "name")
            form.add_formemail("Email", "email")
            form.add_formtextarea("Message", "message")
            form.add_formselect("Options", "options", ["Option 1", "Option 2"])
            form.add_formsubmit("Send!")

    return page


if __name__ == "__main__":
    page = create_page()
    print(page.to_html())
