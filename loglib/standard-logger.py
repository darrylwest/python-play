#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-16 16:23:04

# @see https://docs.python.org/3/library/logging.html for the python docs
# @see https://docs.python.org/3/howto/logging-cookbook.html for improved formatting, file rotation, etc.

import os
import time
from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler, HTTPHandler
import time
from dataclasses import dataclass
from rich import print, inspect
import json
import http.client
from dataclasses import dataclass


@dataclass
class Config:
    name: str = "standard-app"
    level: int = logging.INFO
    filename: str = None
    stream: bool = True
    max_bytes: int = 100_000
    version: str = "0.1.0"


class LogLib:
    @staticmethod
    def create_logger(cfg: Config) -> logging.Logger:
        """create a new logger with or without configuration"""

        lib = LogLib(cfg)

        if cfg.stream:
            lib.init_stream_logger()

        if cfg.filename:
            lib.init_file_logger(cfg.filename)

        return lib.get_logger()

    def __init__(self, config: Config = None):
        cfg = config if config is not None else Config()

        self.cfg = cfg
        self.log = logging.getLogger(cfg.name)
        self.log.setLevel(cfg.level)

    def get_logger(self):
        return self.log

    def get_formatter(self):
        """return the standard log formmater including UTC and nanoseconds"""
        logging.Formatter.converter = time.gmtime
        return logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S.%s",
        )

    def init_stream_logger(self):
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)

        formatter = self.get_formatter()
        handler.setFormatter(formatter)

        self.log.addHandler(handler)

    def init_file_logger(self, filename: str):
        # try to find a logs folder
        path = Path(filename)

        mbytes = self.cfg.max_bytes
        print(f"mbytes: {mbytes}")

        handler = RotatingFileHandler(path, backupCount=5, maxBytes=mbytes)
        handler.setLevel(logging.INFO)

        formatter = self.get_formatter()
        handler.setFormatter(formatter)

        self.log.addHandler(handler)


def standard_config():
    cfg = Config(filename="std-test.log", stream=False, max_bytes=2500)
    inspect(cfg)

    log = LogLib.create_logger(cfg)

    return log


if __name__ == "__main__":
    log = standard_config()

    for n in range(10):
        # log.debug("a debug test")
        log.info("this is an info test {time.time_ns()}...")
        log.info(f"2nd this is an info test {time.time_ns()}...")
        log.warning("warning you")
        log.error("this is an error")
        log.critical("this is CRITICAL")

    print(f"look at the logfile std-test.log")
