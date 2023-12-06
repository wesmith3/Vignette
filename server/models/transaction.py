from config import db
from sqlalchemy_serializer import SerializerMixin
from .user import User
from .artwork import Artwork
from . import validates, re

class Transaction(db.Model, SerializerMixin):
    __tablename__="transactions"
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    seller_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    amount_paid = db.Column(db.Float, nullable=False)
    artwork_id = db.Column(db.Integer, db.ForeignKey("artworks.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())