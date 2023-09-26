from app.extensions.database import CRUD_mixing, db


class Role(db.Model, CRUD_mixing):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)
