from . import fields, validate
from models.like import Like
from config import ma

class LikeSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Like
        load_instance = True
        
    email = fields.Email(required=True)
    password_hash = fields.String(validate=validate.Length(min=10, max=50))