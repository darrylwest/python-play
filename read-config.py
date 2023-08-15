#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-14 18:23:30

# @see https://docs.python.org/3/library/configparser.html

import configparser


def read_config():
    config = configparser.ConfigParser()
    config.read("config/settings.cfg")

    print(config.sections())
    print("compression", config["DEFAULT"]["Compression"])
    print("origins", config["app"]["origins"])
    print("origins", config["app"]["port"])

    for key in config["DEFAULT"]:
        print(key)


if __name__ == "__main__":
    read_config()
