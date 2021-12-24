from .password import Password
from .email import Email
from .pwd_hash import Pwd_hash

from . import auth_db as database

class User(object):
    def __init__(self, username: str="", email=Email(""), firstname: str="", surname: str="", secondsurname: str="", pwd_hash: Pwd_hash=Pwd_hash("", "")):
        self._username = username
        self._email = email
        self._user_id = 0
        self._firstname = firstname
        self._surname = surname
        self._secondsurname = secondsurname
        self._hash = pwd_hash

    def get_user_id(self):
        return self._user_id
    def get_username(self):
        return self._username
    def get_email(self):
        return self._email
    def get_hash(self) -> Pwd_hash:
        return self._hash
    def set_hash(self, pwd_hash: Pwd_hash):
        self._hash = pwd_hash
    def get_firstname(self):
        return self._firstname
    def get_surname(self):
        return self._surname
    def get_secondsurname(self):
        return self._secondsurname

    def get_data(self):
        if (self.get_email() == Email("")):
            return False
        user_data = database.get_user_data(self._email.get_email())
        if (len(user_data) == 0):
            return False
        user_data = user_data[0]
        self._username = user_data["username"]
        self._email = Email(user_data["email"])
        self._hash = Pwd_hash(user_data["pwd_hash"], user_data["pwd_salt"])
        self._user_id = user_data["user_id"]
        self._firstname = user_data["firstname"]
        self._surname = user_data["surname"]
        self._secondsurname = user_data["secondsurname"]
        return True
        
    def register(self) -> bool:
        user_hash = self.get_hash()
        user_email = self.get_email()
        user_data = {
            "username": self.get_username(),
            "email": user_email.get_email(),
            "pwd_hash": user_hash.get_hash(),
            "pwd_salt": user_hash.get_salt(),
            "firstname": self.get_firstname(),
            "surname": self.get_surname(),
            "secondsurname": self.get_secondsurname()
        }
        return database.register_new_user(user_data)
    def login(self, pwd: Password) -> bool:
        if (not self.get_data()):
            return False
        user_hash = self.get_hash()
        pwd_hash = Pwd_hash(
            pwd_hash=user_hash.get_hash(),
            pwd_salt=user_hash.get_salt()
        )
        return pwd_hash.check_password(pwd)
