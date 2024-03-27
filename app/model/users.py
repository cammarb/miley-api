from app.extensions.database import db, CRUD_mixing
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(db.Model, CRUD_mixing, UserMixin):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    passwd = db.Column(db.String(300))
    username = db.Column(db.String(102), unique=True)
    role_id = db.Column(UUID(as_uuid=True), db.ForeignKey("role.id"), nullable=True)
