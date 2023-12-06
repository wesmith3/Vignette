from . import fields, validate
from models.transaction import Transaction
from config import ma

class TransactionSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Transaction
        load_instance = True
        
    email = fields.Email(required=True)
    password_hash = fields.String(validate=validate.Length(min=10, max=50))