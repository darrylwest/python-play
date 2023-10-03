#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-01 14:23:46

import hashlib
import pickle
import sys
from dataclasses import dataclass
from datetime import datetime

from faker import Faker
from rich import inspect, print

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

    return hashed


def test_decode(payload, hash_size: int = 64):
    hash_value = payload[0:hash_size]
    pickled_users = payload[hash_size:]

    print(f"hash length: {len(hash_value)}, user size: {len(pickled_users)}")

    users_hash = test_hash(hashlib.sha3_512(), pickled_users)

    assert hash_value == users_hash

    users = pickle.loads(pickled_users)
    print(users)

    print("decode valid...")


def test_object():
    users = [create_user() for _ in range(10)]
    pickled = pickle.dumps(users)

    inspect(pickled)

    # hash_value = test_hash(hashlib.sha3_256(), pickled)
    hash_value = test_hash(hashlib.sha3_512(), pickled)
    inspect(hash_value)

    value = hash_value + pickled
    inspect(value)

    # now pull the hash and check against payload
    test_decode(value, 64)


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
