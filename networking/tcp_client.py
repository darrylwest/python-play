#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-16 21:29:58

import socket

from rich import print


def connect(port: int = 16000):
    # host = socket.gethostbyname(socket.gethostname())
    host = '127.0.0.1'

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"server connecting to {host}:{port}")

    client.connect((host, port))

    return client


def main() -> None:
    client = connect()

    for n in range(10):
        client.send("rtkey".encode())
        data = client.recv(1024).decode("utf-8")
        msg = data.rstrip()
        print(f"server-> {msg}")

    client.send("bye".encode())
    data = client.recv(1024).decode()
    client.close()


if __name__ == "__main__":
    main()
