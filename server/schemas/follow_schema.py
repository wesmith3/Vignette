from . import fields, validate
from models.follow import Follow
from models.user import User
# from .user_schema import UserSchema

from config import ma

class FollowSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Follow
        load_instance = True

    id = fields.Integer(dump_only=True)
    follower_id = fields.Integer(
        required=True,
        validate=lambda follower_id: Follow.validate_follower_id(follower_id),
        error_messages={"required": "Follower ID is required."},
    )
    following_id = fields.Integer(
        required=True,
        validate=lambda following_id: Follow.validate_following_id(following_id),
        error_messages={"required": "Following ID is required."},
    )
    created_at = fields.DateTime(dump_only=True)
    
    # follower = fields.Nested("UserSchema", exclude=("followers", "following"), dump_only=True)
    # following = fields.Nested("UserSchema", exclude=("followers", "following"), dump_only=True)


    @staticmethod
    def validate_follower_id(follower_id):
        if follower_id and User.query.get(follower_id):
            return follower_id
        raise ValueError('Follower ID must be a valid user.')

    @staticmethod
    def validate_following_id(following_id):
        if following_id and User.query.get(following_id):
            return following_id
        raise ValueError('Following ID must be a valid user.')
