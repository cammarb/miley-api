from app.extensions.database import db, CRUD_mixing
from flask_login import UserMixin


class User(db.Model, CRUD_mixing, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    passwd = db.Column(db.String(300))
    username = db.Column(db.String(102), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False, default=2)
