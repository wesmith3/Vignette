from . import fields, validate
from models.tag import Tag
from config import ma

class TagSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Tag
        load_instance = True
        
    email = fields.Email(required=True)
    password_hash = fields.String(validate=validate.Length(min=10, max=50))