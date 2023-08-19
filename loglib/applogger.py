#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-19 13:48:27
#

# @see https://docs.python.org/3/library/logging.html for the python docs
# @see https://docs.python.org/3/howto/logging-cookbook.html for improved formatting, file rotation, etc.

from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler

class Config:
    def __init__(self):
        self.name = "app"
        self.level = logging.INFO
        self.filename = None
        self.stream = True
        self.max_bytes = 100_000

class LogLib:
    def create_logger(config: Config = None) -> logging.Logger:
        cfg = config if config != None else Config()

        lib = LogLib(cfg.name, cfg.level)
        if cfg.stream:
            lib.init_stream_logger()

        if cfg.filename:
            lib.init_file_logger(cfg.filename)

        return lib.get_logger()

    def __init__(self, name: str = "app", level: int = logging.INFO):
        cfg = Config()
        cfg.name = name
        cfg.level = level

        self.cfg = cfg
        self.log = logging.getLogger(name)
        self.log.setLevel(level)

    def get_logger(self):
        return self.log

    def init_stream_logger(self):
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)

        self.log.addHandler(handler)


    def init_file_logger(self, filename: str):
        # try to find a logs folder
        path = Path(filename)

        mbytes = self.cfg.max_bytes

        handler = RotatingFileHandler(path, backupCount=5, maxBytes=mbytes)
        handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)

        self.log.addHandler(handler)




if __name__ == "__main__":
    # confingure log lib
    # loglib = LogLib()
    # loglib.init_stream_logger()
    # loglib.init_file_logger("test-1.log")

    # get the log
    cfg = Config()
    cfg.filename = "test.log"
    log = LogLib.create_logger(cfg)

    # test it
    log.debug("a debug test")
    log.info("this is an info test...")
    log.warning("warning you")
    log.error("this is an error")
    log.critical("this is CRITICAL")

    print(f"look at the logfile test-?")


