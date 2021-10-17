import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    with app.app_context():
        #from . import auth
        from . import routes
        
        #app.register_blueprint(auth.bp)
        app.register_blueprint(routes.bp)

        return app
