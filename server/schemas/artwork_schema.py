from . import fields, validate
from models.artwork import Artwork
from config import ma

class ArtworkSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Artwork
        load_instance = True
        
    email = fields.Email(required=True)
    password_hash = fields.String(validate=validate.Length(min=10, max=50))