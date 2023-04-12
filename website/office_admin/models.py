from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



#Users table in master_db
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    usertype = db.Column(db.String(150))
    department = db.Column(db.String(150))