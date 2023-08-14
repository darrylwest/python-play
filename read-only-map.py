#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-27 13:52:22

import begin
from types import MappingProxyType


def create_writable():
    rw = {"one": 1, "two": 2, "three": 3}

    return rw


def create_read_only(mp):
    read_only = MappingProxyType(mp)

    return read_only


@begin.start
def main(arg1=None):
    w = create_writable()
    ro = create_read_only(w)

    print(f"read only {ro}")

    w["three"] = 42

    print(f"read only {ro}")

    # this is not possible
    # ro['two'] = 9
