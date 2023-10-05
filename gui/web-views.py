#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-02 13:55:25

import sys

import webview
from rich import inspect, print


def get_elements(window):
    user = window.get_elements("#rcmloginuser")[0]
    # user['attributes']['value'] = 'dpw500@raincitysoftware.com'
    inspect(user)
    for k, v in user.items():
        print(k, v, type(v))


def main(args: list) -> None:
    # print(f'{args}')
    # url = 'https://raincitysoftware.com'
    # url = 'https://darrylwest.github.io/'

    url = "https://webmail.dreamhost.com/?clearSession=true&_user=dpw500@raincitysoftware.com"

    window = webview.create_window(
        title="Web Mail",
        url=url,
        width=1200,
        height=1000,
        frameless=False,
        js_api=True,
    )

    webview.start(get_elements, window, debug=True, user_agent="dpw")


if __name__ == "__main__":
    main(sys.argv[1:])
