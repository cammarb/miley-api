from api.extensions.database import db, CRUD_mixing


class SongWriter(db.Model, CRUD_mixing):
    song_id = db.Column(db.Integer, db.ForeignKey(
        'song.id'), primary_key=True)
    writer_id = db.Column(db.Integer, db.ForeignKey(
        'writer.id'), primary_key=True)
