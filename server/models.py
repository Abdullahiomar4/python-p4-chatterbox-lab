# server/models.py

from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import func
from config import db

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    serialize_rules = ()

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )
