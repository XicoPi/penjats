import os
from flask import Flask
from flask_restful import Api



def init():
    return None

def init_api_resources(app):
    api = Api(app)
    from .api import auth as authApiModule
    api.add_resource(authApiModule.Login, "/api/login")
    api.add_resource(authApiModule.Register, "/api/register")
    return api

def create_app(test_config=None):
    init()
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    from .routes import auth
    auth.login_manager.init_app(app)
    auth.login_manager.session_protection = "strong"

    #API
    api = init_api_resources(app)
    api.init_app(app)

    with app.app_context():
        from .routes import main
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(main.main_bp)
        return app
