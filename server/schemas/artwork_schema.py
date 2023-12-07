from . import fields
from models.artwork import Artwork
from models.user import User
# from .user_schema import UserSchema
# from .comment_schema import CommentSchema
# from .like_schema import LikeSchema
# from .tag_schema import TagSchema
# from config import ma


class ArtworkSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Artwork
        load_instance = True

    # user = fields.Nested("UserSchema", exclude=("artworks",))
    # likes = fields.Nested("LikeSchema", exclude=("artwork",))
    # comments = fields.Nested("CommentSchema", exclude=("artwork",))
    # tags = fields.Nested("TagSchema", exclude=("artworks",))

    user_id = fields.Integer(
        required=True,
        validate=lambda user_id: Artwork.validate_user_id(user_id),
        error_messages={"required": "User ID is required."},
    )

    title = fields.String(
        validate=lambda s: 1 <= len(s) <= 130,
        required=True,
        error_messages={
            "required": "Title is required.",
            "validator_failed": "Title must be between 1 and 130 characters.",
        },
    )
    description = fields.String(
        validate=lambda s: len(s) <= 300,
        error_messages={
            "validator_failed": "Description cannot be longer than 300 characters."
        },
    )
    image = fields.String(
        required=True, error_messages={"required": "Image is required."}
    )
    price = fields.Float(
        validate=lambda p: p >= 0,
        required=True,
        error_messages={
            "required": "Price is required.",
            "validator_failed": "Price must be a non-negative number.",
        },
    )
    preview = fields.Boolean(
        required=True, error_messages={"required": "Preview is required."}
    )

    @staticmethod
    def validate_user_id(user_id):
        if user_id and User.query.get(user_id):
            return user_id
        raise ValueError("User ID must be a valid user.")