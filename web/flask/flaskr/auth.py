from flask_login import LoginManager
from objects import user

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    query = "select id_user, username, email, firstname, surname, secondsurname from users"
