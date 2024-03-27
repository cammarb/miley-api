from app.extensions.database import CRUD_mixing, db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Role(db.Model, CRUD_mixing):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(25), unique=True)
