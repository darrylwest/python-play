#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-16 20:29:26

import socket


def myip() -> str:
    return socket.gethostbyname(socket.gethostname())


if __name__ == "__main__":
    print(myip())
