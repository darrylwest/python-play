#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-02 13:55:25

import sys

import webview
from rich import print


def main(args: list) -> None:
    # print(f'{args}')
    webview.create_window("howdy yall", "https://pywebview.flowrl.com/")
    webview.start()


if __name__ == "__main__":
    main(sys.argv[1:])
