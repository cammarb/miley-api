from app.extensions.database import CRUD_mixing, db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Artist(db.Model, CRUD_mixing):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String)
    tracks = db.relationship(
        "TrackArtist", back_populates="artist", cascade="all, delete-orphan"
    )


class TrackArtist(db.Model, CRUD_mixing):
    track_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("track.id"), primary_key=True
    )
    artist_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("artist.id"), primary_key=True
    )
    track = db.relationship("Track", back_populates="featuring_artists")
    artist = db.relationship("Artist", back_populates="tracks")
