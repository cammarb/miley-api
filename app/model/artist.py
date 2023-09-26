from app.extensions.database import CRUD_mixing, db


class Artist(db.Model, CRUD_mixing):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    albums = db.relationship(
        "Album", backref="artist", lazy=True, cascade="all, delete-orphan"
    )
