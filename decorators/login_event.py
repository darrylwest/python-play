#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-15 22:21:18

from dataclasses import dataclass
from datetime import datetime

import typer


def hide_field(field) -> str:
    """redact the password"""
    return "**redacted**"


def format_timestamp(field_timestamp) -> str:
    """format to rfc_3339 UTC"""
    return field_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%sZ")


def show_original(event_field):
    """do a simple passthrough"""
    return event_field


class EventSerializer:
    def __init__(self, serialization_fields: dict) -> None:
        self.serialization_fields = serialization_fields

    def serialize(self, event) -> dict:
        return {
            field: transformation(getattr(event, field))
            for field, transformation in self.serialization_fields.items()
        }


class Serialization:
    def __init__(self, **transformations):
        self.serializer = EventSerializer(transformations)

    def __call__(self, event_class):
        def serialize_method(event_instance):
            return self.serializer.serialize(event_instance)

        event_class.serialize = serialize_method
        return event_class


@Serialization(
    username=str.lower,
    password=hide_field,
    ip=show_original,
    timestamp=format_timestamp,
)
@dataclass
class LoginEvent:
    username: str
    password: str
    ip: str
    timestamp: datetime


def main(username: str, password: str) -> None:
    from rich.console import Console

    console = Console()

    now = datetime.now()
    console.log(f"create login for {username} at {now}")
    event = LoginEvent(
        username=username,
        password=password,
        ip="127.0.0.1",
        timestamp=now,
    )

    console.log(event.serialize())


def test_event():
    now = datetime.now()
    event = LoginEvent(
        username="flarb",
        password="12345",
        ip="127.0.0.1",
        timestamp=now,
    )
    ser = event.serialize()
    assert ser["username"] == event.username
    assert ser["password"] == "**redacted**"
    assert ser["ip"] == event.ip

    # assert ser.timestamp =


if __name__ == "__main__":
    typer.run(main)
