from app.extensions.database import CRUD_mixing, db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Album(db.Model, CRUD_mixing):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String, nullable=False, unique=True)
    slug = db.Column(db.String, nullable=False, unique=True)
    release_date = db.Column(db.Date, nullable=False)
    tracks = db.relationship(
        "Track", back_populates="album", cascade="all, delete-orphan"
    )
    total_length = db.Column(db.String)
