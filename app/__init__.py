#app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'authentication.signin_user'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()

def create_app(config_type):

    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')

    app.config.from_pyfile(configuration)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app.movies import main 
    app.register_blueprint(main) 

    from app.auth import authentication
    app.register_blueprint(authentication)

    return app