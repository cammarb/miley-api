from app.extensions.database import CRUD_mixing, db


class Album(db.Model, CRUD_mixing):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    slug = db.Column(db.String, nullable=False, unique=True)
    release_date = db.Column(db.Date, nullable=False)
    is_live = db.Column(db.Boolean)  # if True, album is live version
    is_ep = db.Column(db.Boolean)  # if True, it's an EP (Extended Play)
    number_of_songs = db.Column(db.Integer)
    tracklist = db.relationship(
        "Song", back_populates="album", cascade="all, delete-orphan"
    )
    total_length = db.Column(db.String)
    artist_id = db.Column(db.Integer, db.ForeignKey("artist.id"), nullable=False)
