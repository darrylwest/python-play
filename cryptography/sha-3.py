#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-01 14:23:46

import sys
from rich import print, inspect
from dataclasses import dataclass
from datetime import datetime
from faker import Faker
import pickle

import hashlib

fake = Faker()


@dataclass
class TestUser:
    id: int
    name: str
    created: datetime
    age: int
    description: str
    friends: list


def create_user():
    user = TestUser(
        id=fake.unique.random_int(),
        name=fake.name(),
        created=datetime.utcnow(),
        age=fake.random_int(min=10, max=50),
        description=fake.sentence(),
        friends=[fake.first_name(), fake.first_name(), fake.first_name()],
    )

    print(user)
    return user


def test_hash(hasher, bytes):
    hasher.update(bytes)
    hashed = hasher.digest()
    hex = hasher.hexdigest()
    print(f"hasher: {hasher.name}")
    print(f"bin length: {len(hashed)}", hashed)
    print(f"hex length: {len(hex)}", hex)


def test_object():
    user = create_user()


def test_message():
    text = b"Good day, planet earth!"

    print(f"message: {text}")

    test_hash(hashlib.sha3_224(), text)
    test_hash(hashlib.sha3_256(), text)
    test_hash(hashlib.sha3_384(), text)
    test_hash(hashlib.sha3_512(), text)


def main(args: list) -> None:
    if len(args) == 0:
        test_message()
        test_object()

    if "message" in args:
        test_message()

    if "obj" in args:
        test_object()


if __name__ == "__main__":
    main(sys.argv[1:])
