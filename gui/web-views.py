#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-02 13:55:25

import sys

import screeninfo
import webview
from rich import inspect, print


def get_elements(window):
    # inspect(window)
    # user = window
    return


def parse(arg: str) -> str:
    match arg:
        case "dpw":
            return "https://webmail.dreamhost.com/?clearSession=true&_user=dpw@raincitysoftware.com&_pass=mypass"
        case "dpw500":
            return "https://webmail.dreamhost.com/?clearSession=true&_user=dpw500@raincitysoftware.com&_pass=mypass"
        case "rcs":
            return "https://raincitysoftware.com"
        case "you":
            return "https://wwww.youtube.com"
        case "python":
            return "https://python.org"
        case "real":
            return "https://realpython.com"
        case other:
            return "https://google.com"


def main(args: list) -> None:
    # url = 'https://darrylwest.github.io/'

    match len(args):
        case 0:
            url = "https://www.youtube.com/"
        case 1:
            url = parse(args[0])
        case other:
            if "--url" in args:
                url = args[1]

    monitor = screeninfo.get_monitors()[0]

    window = webview.create_window(
        title="Web",
        url=url,
        width=monitor.width - 60,
        height=monitor.height - 60,
        frameless=False,
        js_api=True,
    )

    webview.start(get_elements, window, debug=True, user_agent="dpw")


if __name__ == "__main__":
    main(sys.argv[1:])
