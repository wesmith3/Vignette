from . import fields
from models.transaction import Transaction
from models.artwork import Artwork
from models.user import User
from config import ma


class TransactionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Transaction
        load_instance = True

    id = fields.Integer(dump_only=True)
    buyer_id = fields.Integer(
        required=True,
        validate=lambda buyer_id: Transaction.validate_buyer_id(buyer_id),
        error_messages={"required": "Buyer ID is required."},
    )
    seller_id = fields.Integer(
        required=True,
        validate=lambda seller_id: Transaction.validate_seller_id(seller_id),
        error_messages={"required": "Seller ID is required."},
    )
    amount_paid = fields.Float(
        required=True,
        validate=lambda amount_paid: Transaction.validate_amount_paid(amount_paid),
        error_messages={
            "required": "Amount paid is required.",
            "validator_failed": "Amount paid must be a non-negative number.",
        },
    )
    artwork_id = fields.Integer(
        required=True,
        validate=lambda artwork_id: Transaction.validate_artwork_id(artwork_id),
        error_messages={"required": "Artwork ID is required."},
    )
    created_at = fields.DateTime(dump_only=True)

    @staticmethod
    def validate_buyer_id(buyer_id):
        if buyer_id and User.query.get(buyer_id):
            return buyer_id
        raise ValueError("Buyer ID must be a valid user.")

    @staticmethod
    def validate_seller_id(seller_id):
        if seller_id and User.query.get(seller_id):
            return seller_id
        raise ValueError("Seller ID must be a valid user.")

    @staticmethod
    def validate_amount_paid(amount_paid):
        if amount_paid is not None and amount_paid >= 0:
            return amount_paid
        raise ValueError("Amount paid must be a non-negative number.")

    @staticmethod
    def validate_artwork_id(artwork_id):
        if artwork_id and Artwork.query.get(artwork_id):
            return artwork_id
        raise ValueError("Artwork ID must be a valid artwork.")
