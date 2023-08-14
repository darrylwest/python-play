#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-02 16:13:15

import begin
import secrets
import string

# secrets is preferrable to random (see PEP506)
# a better approach would be to implement rules, like at least 2 upper, 2 lower, 2 numbers, 2 chars, no repeats, etc


def define_chars():
    others = "#$%&()*+,-.:;=?@^_`|!"
    chars = string.ascii_letters + string.digits + others

    return chars


def generate_password(chars, length):
    password = "".join(secrets.choice(chars) for i in range(length))

    return password


@begin.start
def main(arg1=None):
    chars = define_chars()
    pw = generate_password(chars, 20)

    print(f"{pw}")
