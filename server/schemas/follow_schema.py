from . import fields, validate
from models.follow import Follow
from config import ma

class FollowSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Follow
        load_instance = True
        
    email = fields.Email(required=True)
    password_hash = fields.String(validate=validate.Length(min=10, max=50))