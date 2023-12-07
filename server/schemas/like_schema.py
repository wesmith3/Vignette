from . import fields
from models.like import Like
from models.artwork import Artwork
from models.user import User
# from .artwork_schema import ArtworkSchema
# from .user_schema import UserSchema

from config import ma


class LikeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Like
        load_instance = True

    user_id = fields.Integer(
        required=True,
        validate=lambda user_id: Like.validate_user_id(user_id),
        error_messages={"required": "User ID is required."},
    )
    artwork_id = fields.Integer(
        required=True,
        validate=lambda artwork_id: Like.validate_artwork_id(artwork_id),
        error_messages={"required": "Artwork ID is required."},
    )
    created_at = fields.DateTime(dump_only=True)

    # artwork = fields.Nested("ArtworkSchema", exclude=("likes",), dump_only=True, many=False)
    # user = fields.Nested("UserSchema", exclude=("likes",))

    @staticmethod
    def validate_user_id(user_id):
        if user_id and User.query.get(user_id):
            return user_id
        raise ValueError("User ID must be a valid user.")

    @staticmethod
    def validate_artwork_id(artwork_id):
        if artwork_id and Artwork.query.get(artwork_id):
            return artwork_id
        raise ValueError("Artwork ID must be connected to a valid artwork.")

