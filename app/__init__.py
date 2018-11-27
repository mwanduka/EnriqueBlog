from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_simplemde import SimpleMDE
from flask_login import LoginManager,current_user
from flask_mail import Mail
from flask_admin import Admin

admin = Admin()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
simple = SimpleMDE()
mail = Mail()


def create_app(config_state):
    app = Flask(__name__)
    app.config.from_object(config_options[config_state])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    simple.init_app(app)
    mail.init_app(app)
    admin.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    return app
