from flask_login import UserMixin
#from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, user_id, name="", email="", user_type=""):
        self.id = user_id
        self.username = name
        self.email = email
        self.pwd_hash = ""
        self.type_user = user_type
    def __repr__(self):
        return '<User {}>'.format(self.email)
    
