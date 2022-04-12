from api.extensions.database import db


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    release_date = db.Column(
        db.Date(), nullable=False)
    songs = db.relationship('Song', backref='album', lazy=True)
    total_length = db.Column(db.String(10))
