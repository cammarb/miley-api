from app.extensions.database import CRUD_mixing, db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Track(db.Model, CRUD_mixing):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String, nullable=False, unique=True)
    slug = db.Column(db.String, nullable=False, unique=True)
    length = db.Column(db.String, nullable=False)
    album_id = db.Column(UUID(as_uuid=True), db.ForeignKey("album.id"), nullable=True)
    album = db.relationship("Album", back_populates="tracks")
    featuring_artists = db.relationship(
        "TrackArtist", back_populates="track", cascade="all, delete-orphan"
    )
