from app.extensions.database import db


class Producer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    song_producers = db.relationship(
        'SongProducer', backref='producer', lazy=True)
