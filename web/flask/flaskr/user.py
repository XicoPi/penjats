from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, id, name, email, password, user_type):
        self.id = id
        self.username = name
	self.email = email
	self.password = password
        self.type_user = user_type

    def __repr__(self):
        return '<User {}>'.format(self.email)
