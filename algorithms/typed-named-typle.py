#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-13 22:36:26

import sys
from rich import inspect, print
from typing import NamedTuple, Self


class Config(NamedTuple):
    host: str
    port: int
    scheme: str = "https://"

    @staticmethod
    def url(cfg: Self, uri: str) -> str:
        return "".join([cfg.scheme, cfg.host, ":", str(cfg.port), uri])


def main(args: list) -> None:
    print(f"{args}")
    cfg = Config(host="localhost", port=3000)

    inspect(Config)
    inspect(cfg)

    print(f"url: {Config.url(cfg, '/api/v1/ping')}")

    # will raise
    # cfg.port = 33


if __name__ == "__main__":
    main(sys.argv[1:])
