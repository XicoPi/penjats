import crypt
import re

from flask import Blueprint, request, url_for, flash, redirect, render_template
from flask_login import LoginManager, login_required, logout_user, current_user, login_user
from ..objects import user


#from . import database


login_manager = LoginManager()
auth_bp = Blueprint(
    'auth_bp',
    __name__,
    template_folder="templates",
    static_folder="static"
)

def check_password(password: str):
    result = True
    if ((len(password) < 8) or (re.search("[0-9]", password) is None) or (re.search("[A-Z]", password) is None)):
        result = False
    return result

@auth_bp.route("/login", methods=("GET",))
def login():
    if (current_user.is_authenticated):
        return redirect(url_for("main_bp.index"))
    return render_template("auth/login.html")

@auth_bp.route("/login_fail", methods=["GET"])
def login_fail():
    return render_template("auth/login_failed.html")

@auth_bp.route("/register", methods=("GET",))
def register():
    if (current_user.is_authenticated):
        return redirect(url_for("main_bp.index"))
    return render_template("auth/register.html")

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main_bp.index"))
        
@login_manager.user_loader
def load_user(user_id):
    return user.User(user_id)
    
