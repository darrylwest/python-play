from rich import inspect, print


# content of emaillib.py
class MailAdminClient:
    def create_user(self):
        print("create the mail user: admin")
        return MailUser("admin")

    def delete_user(self, user):
        print(f"delete the mail user: {user.name}")
        pass


class MailUser:
    def __init__(self, name):
        self.name = name
        self.inbox = []

    def send_email(self, email, other):
        print(f"send the email: {email}")
        other.inbox.append(email)
        inspect(self.inbox)

    def clear_mailbox(self):
        print("clear the inbox:")
        inspect(self.inbox)
        self.inbox.clear()


class Email:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body
