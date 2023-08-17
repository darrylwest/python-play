#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-17 15:43:38

import typer
from rich import print

import socket


def scan(ipaddr: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((ipaddr, port))
    isopen = result == 0
    sock.close()

    return isopen


def main(ipaddr: str, start_port: int, end_port: int) -> None:
    print(f"scan ports on {ipaddr} from {start_port} to {end_port}")

    for port in range(start_port, end_port + 1):
        open = scan(ipaddr, port)
        print(f"{port} is open") if open else print(f"{port} is open")


if __name__ == "__main__":
    typer.run(main)
