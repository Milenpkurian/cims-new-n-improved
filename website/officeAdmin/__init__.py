from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .config import master_db

db = SQLAlchemy()
DB_NAME = master_db


def create_app():
    app = Flask(__name__)

    # Secret Key Generation
    import secrets
    secret_key = secrets.token_hex(16)
    # example output, secret_key = 000d88cd9d90036ebdd237eb6b0dep000
    app.config['SECRET_KEY'] = secret_key

    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')