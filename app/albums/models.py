from app.extensions.database import db, CRUD_mixing


class Album(db.Model, CRUD_mixing):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    release_date = db.Column(
        db.Date(), nullable=False)
    songs = db.relationship('Song', backref='album', lazy=True)
