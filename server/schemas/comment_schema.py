from . import fields
from models.comment import Comment
from models.artwork import Artwork
from models.user import User
# from .artwork_schema import ArtworkSchema
# from .user_schema import UserSchema

from config import ma


class CommentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Comment
        load_instance = True

    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(
        required=True,
        validate=lambda user_id: Comment.validate_user_id(user_id),
        error_messages={"required": "User ID is required."},
    )
    artwork_id = fields.Integer(
        required=True,
        validate=lambda artwork_id: Comment.validate_artwork_id(artwork_id),
        error_messages={"required": "Artwork ID is required."},
    )
    content = fields.String(
        required=True,
        validate=lambda c: Comment.validate_content(c),
        error_messages={
            "required": "Content is required.",
            "validator_failed": "Content must be between 1 and 150 characters.",
        },
    )
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    
    # artwork = fields.Nested("ArtworkSchema", exclude=("comments",), dump_only=True, many=False)
    # user = fields.Nested("UserSchema", exclude=("comments",))

    @staticmethod
    def validate_user_id(user_id):
        if user_id and User.query.get(user_id):
            return user_id
        raise ValueError("User ID must be a valid user.")

    @staticmethod
    def validate_artwork_id(artwork_id):
        if artwork_id and Artwork.query.get(artwork_id):
            return artwork_id
        raise ValueError("Artwork ID must be a valid artwork.")

    @staticmethod
    def validate_content(content):
        if content and 1 <= len(content) <= 150:
            return content
        raise ValueError("Content must be between 1 and 150 characters.")
