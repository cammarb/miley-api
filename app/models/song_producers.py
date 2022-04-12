from app.extensions.database import db, CRUD_mixing


class SongProducer(db.Model, CRUD_mixing):
    song_id = db.Column(db.Integer, db.ForeignKey(
        'song.id'), primary_key=True)
    producer_id = db.Column(db.Integer, db.ForeignKey(
        'producer.id'), primary_key=True)
