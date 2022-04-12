from api.extensions.database import db


class Writer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    song_writers = db.relationship('SongWriter', backref='writer', lazy=True)
