import crypt
from .password import Password

class Pwd_hash(object):
    def __init__(self, pwd_hash: str="", pwd_salt: str=""):
        self._pwd_hash = pwd_hash
        self._pwd_salt = pwd_salt
    def get_hash(self):
        return self._pwd_hash
    def get_salt(self):
        return self._pwd_salt
    def check_password(self, pwd: Password) -> bool:
        test_pwd_hash = crypt.crypt(
            word=pwd.get_password(),
            salt=self.get_salt()
        )
        return test_pwd_hash == self.get_hash()
    def generate(self, pwd: Password):
        self._pwd_salt = crypt.mksalt(
            method=crypt.METHOD_SHA512
        )
        self._pwd_hash = crypt.crypt(
            word=pwd.get_password(),
            salt=self._pwd_salt
        )
