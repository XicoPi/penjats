import crypt
import json

from flask_restful import Resource
from flask import request
from flask_login import login_user, current_user

#project
from ..objects import user as db_user
from .objects.auth.user import User
from .objects.auth.email import Email
from .objects.auth.password import Password
from .objects.auth.pwd_hash import Pwd_hash


class Login(Resource):
    def post(self):
        if (current_user.is_authenticated):
            return ({}, 200)
        try:
            req_body = json.loads(request.get_data())
        except:
            return ({}, 400) #Bad Request

        user = User(
            email=Email(req_body["email"])
        )
        if (not user.login(Password(req_body["pwd"]))):
            return ({}, 404)
        session_user = db_user.User(
            user_id=user.get_user_id()
        )
        login_user(session_user)
        return ({}, 200)

class Register(Resource):
    def post(self):
        if (current_user.is_authenticated):
            return ({}, 200)
        try:
            req_body = json.loads(request.get_data())
        except:
            return ({}, 400)
        email = Email(req_body["email"])
        pwd_0 = Password(req_body["pwd_0"])
        pwd_1 = Password(req_body["pwd_1"])
        
        if (pwd_0 != pwd_1 or not pwd_0.check_format()):
            res_body = {
                "error": "Passwords"
            }
            return (res_body, 404)
        if (not email.check_format()):
            res_body = {
                "error": "Bad-Format email"
            }
            return (res_body, 404)
        pwd_hash = Pwd_hash()
        pwd_hash.generate(pwd_0)
        user = User(
            email=email,
            pwd_hash=pwd_hash,
            username=req_body["username"],
            firstname=req_body["firstname"],
            surname=req_body["surname"]
        )
        if (not user.register()):
            return ({}, 404)
        user.get_data()
        session_user = db_user.User(
            user_id=user.get_user_id(),
            name=user.get_username(),
            email=user.get_email()
        )
        login_user(session_user)
        return ({}, 200)

    

    
