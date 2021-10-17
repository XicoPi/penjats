import os
from flask import Flask
from flask_restful import Api
#from flask_login import LoginManager
from . import auth



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    auth.login_manager.init_app(app)
    with app.app_context():
        #from . import auth
        from . import routes
        
        #app.register_blueprint(auth.bp)
        app.register_blueprint(routes.bp)

        return app
