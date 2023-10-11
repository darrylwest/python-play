#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-30 13:19:27

#
# @see: https://docs.pytest.org/en/latest/how-to/fixtures.html
# The safest and simplest fixture structure requires limiting fixtures to only making one state-changing
# action each, and then bundling them together with their teardown code, as the email examples above showed.
#

import sys

import pytest
# content of test_emaillib.py
from emaillib import Email, MailAdminClient
from rich import print


@pytest.fixture
def mail_admin():
    print("FIXTURE: create the admin client")
    return MailAdminClient()


@pytest.fixture
def sending_user(mail_admin):
    print("FIXTURE: setup create user")
    user = mail_admin.create_user()
    yield user
    print("FIXTURE: teardown delete user")
    mail_admin.delete_user(user)


@pytest.fixture
def receiving_user(mail_admin):
    print("FIXTURE: setup receiving user")
    user = mail_admin.create_user()
    yield user
    print("FIXTURE: teardown clear mailbox")
    user.clear_mailbox()
    mail_admin.delete_user(user)


def test_email_received(sending_user, receiving_user):
    email = Email(subject="Hey!", body="How's it going?")
    sending_user.send_email(email, receiving_user)
    assert email in receiving_user.inbox


if __name__ == "__main__":
    print(f"run this: pytest -s {sys.argv[0]}")
