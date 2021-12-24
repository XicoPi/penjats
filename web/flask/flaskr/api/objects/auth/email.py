import re

class Email(object):
    def __init__(self, email: str):
        self._email = email
    def __eq__(self, test) -> bool:
        return self.get_email() == test.get_email()
    def get_email(self):
        return self._email
    def check_format(self) -> bool:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.fullmatch(regex, self.get_email())
