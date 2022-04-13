from api.extensions.database import db, CRUD_mixing


class Song(db.Model, CRUD_mixing):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(300))
    title = db.Column(db.String(300))
    single = db.Column(db.Boolean)
    album_id = db.Column(db.Integer, db.ForeignKey(
        'album.id'))
    song_writers = db.relationship('SongWriter', backref='song', lazy=True)
    length = db.Column(db.String(10))
