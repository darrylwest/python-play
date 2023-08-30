#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-19 13:48:27
#

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
    name: str = "app"
    level: int = logging.INFO
    filename: str = None
    stream: bool = True
    host: str = None
    uri: str = None
    max_bytes: int = 100_000
    version: str = "0.1.0"


@dataclass
class LogModel:
    name: str
    msg: str
    level: str
    filename: str
    lineno: int
    created: float
    asctime: str
    other: list


class JSONHTTPHandler(HTTPHandler):
    def mapLogRecord(self, record):
        """
        Override this method to map the log record into a dict that can be converted to JSON.
        """
        model = LogModel(
            record.name,
            record.message,
            record.levelname,
            record.filename,
            record.lineno,
            record.created,
            record.asctime,
            [],
        )

        return model.__dict__

    def emit(self, record):
        """
        Override this method to send data in JSON format.
        """
        try:
            host = self.host
            url = self.url
            data = json.dumps(self.mapLogRecord(record))

            headers = {
                "Content-type": "application/json",
                "Content-length": str(len(data)),
            }
            if self.secure:
                h = http.client.HTTPSConnection(host)
            else:
                h = http.client.HTTPConnection(host)
            h.request("POST", url, data, headers)
            h.getresponse()
        except Exception:
            self.handleError(record)


class LogLib:
    @staticmethod
    def create_logger(config: Config = None) -> logging.Logger:
        """create a new logger with or without configuration"""
        cfg = config if config != None else Config()

        lib = LogLib(cfg.name, cfg.level)
        if cfg.stream:
            lib.init_stream_logger()

        if cfg.filename:
            lib.init_file_logger(cfg.filename)

        if cfg.host != None and cfg.uri != None:
            lib.init_html_logger(cfg.host, cfg.uri)

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

        handler = RotatingFileHandler(path, backupCount=5, maxBytes=mbytes)
        handler.setLevel(logging.INFO)

        formatter = self.get_formatter()
        handler.setFormatter(formatter)

        self.log.addHandler(handler)

    def init_html_logger(self, host, uri):
        handler = JSONHTTPHandler(host, uri, method="POST")

        handler.setLevel(logging.INFO)
        self.log.addHandler(handler)


if __name__ == "__main__":
    # confingure log lib
    # loglib = LogLib()
    # loglib.init_stream_logger()
    # loglib.init_file_logger("test-1.log")

    # get the log
    cfg = Config()
    # cfg.filename = "test.log"

    # should ping the host before enabling; see web/webapp.py for an example server
    host = os.getenv("LOCAL_IP")
    cfg.host = f"{host}:15010"
    # cfg.host = '127.0.0.1:15010'
    cfg.uri = "/v1/logit/app"

    log = LogLib.create_logger(cfg)

    # test it
    # log.debug("a debug test")
    log.info(f"this is an info test {time.time_ns()}...")
    log.info(f"2nd this is an info test {time.time_ns()}...")
    log.warning("warning you")
    log.error("this is an error")
    # log.critical("this is CRITICAL")

    print(f"look at the logfile test-?")
