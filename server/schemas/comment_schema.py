from . import fields, validate
from models.comment import Comment
from config import ma

class CommentSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Comment
        load_instance = True
        
    email = fields.Email(required=True)
    password_hash = fields.String(validate=validate.Length(min=10, max=50))