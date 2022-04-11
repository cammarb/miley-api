from app.extensions.database import db


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    album_id = db.Column(db.Integer, db.ForeignKey(
        'album.id'))
