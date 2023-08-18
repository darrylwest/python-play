#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-19 13:48:27
#

# @see https://docs.python.org/3/library/logging.html for the python docs
# @see https://docs.python.org/3/howto/logging-cookbook.html for improved formatting, file rotation, etc.

import logging

log = logging.getLogger("app")
log.setLevel(logging.DEBUG)


def init_stream_logger():
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    log.addHandler(handler)


def init_file_logger(fname):
    handler = logging.FileHandler(fname)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    log.addHandler(handler)


def test_logging():
    log.debug("a debug test")
    log.info("this is an info test...")
    log.warning("warning you")
    log.error("this is an error")
    log.critical("this is CRITICAL")

    print(f"look at the logfile test-?")


if __name__ == "__main__":
    init_stream_logger()
    init_file_logger("test-1.log")
    test()
