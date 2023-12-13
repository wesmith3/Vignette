from config import db
from sqlalchemy_serializer import SerializerMixin
from .user import User
from .artwork import Artwork
from . import validates, re


class Transaction(db.Model, SerializerMixin):
    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    amount_paid = db.Column(db.Float, nullable=False)
    artwork_id = db.Column(db.Integer, db.ForeignKey("artworks.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Relationships
    buyer = db.relationship(
        "User", foreign_keys=[buyer_id], back_populates="buyer_transactions"
    )
    artwork = db.relationship("Artwork", back_populates="transactions")

    # Serialization
    serialize_rules=("-buyer.buyer_transactions", "-seller.seller_transactions")
    serialize_only = (
        "id",
        "buyer_id",
        "amount_paid",
        "artwork_id",
        "created_at",
        "artwork.title"
    )

    # Validations
    @validates("buyer_id")
    def buyer_id_validation(self, key, buyer_id):
        if buyer_id and User.query.get(buyer_id):
            return buyer_id
        else:
            raise ValueError("Buyer ID must be a valid user.")

    @validates("amount_paid")
    def amount_paid_validation(self, key, amount_paid):
        if amount_paid is not None and amount_paid >= 0:
            return amount_paid
        else:
            raise ValueError("Amount paid must be a non-negative number.")

    @validates("artwork_id")
    def artwork_id_validation(self, key, artwork_id):
        if artwork_id and Artwork.query.get(artwork_id):
            return artwork_id
        else:
            raise ValueError("Artwork ID must be a valid artwork.")
