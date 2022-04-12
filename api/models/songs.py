from api.extensions.database import db


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    album_id = db.Column(db.Integer, db.ForeignKey(
        'album.id'))
    song_writers = db.relationship('SongWriter', backref='song', lazy=True)
    song_producers = db.relationship('SongProducer', backref='song', lazy=True)
