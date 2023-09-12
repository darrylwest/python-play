#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-02 16:47:30

# ref: https://betterstack.com/community/guides/logging/structlog/
# ref

import sys
from rich import print
import structlog

logger = structlog.get_logger()


def main(args: list) -> None:
    # print(f'{args}')
    logger.debug("hi debug")
    logger.info("hi info")
    logger.warning("hi warning")
    logger.error("hi error")
    logger.critical("hi critical")


if __name__ == "__main__":
    main(sys.argv[1:])
