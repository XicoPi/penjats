import re

class Password(object):
    def __init__(self, pwd: str):
        self._pwd = pwd
    def get_password(self):
        return self._pwd
    def check_format(self) -> bool:
        result = True
        if ((len(self.get_password()) < 8) or (re.search("[0-9]", self.get_password()) is None) or (re.search("[A-Z]", self.get_password()) is None)):
            result = False
        return result
    def __eq__(self, test_pwd) -> bool:
        return (self.get_password() == test_pwd.get_password())
