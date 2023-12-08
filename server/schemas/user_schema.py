from . import fields, validates
from models.user import User
from config import ma

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = fields.Integer(dump_only=True)
    full_name = fields.String(
        validate=lambda s: 1 <= len(s) <= 150,
        required=True,
        error_messages={
            "required": "Full name is required.",
            "validator_failed": "Full name must be between 1 and 150 characters.",
        },
    )
    username = fields.String(
        required=True, error_messages={"required": "Username is required."}
    )
    email = fields.String(
        validate=lambda e: len(e) <= 130,
        required=True,
        error_messages={
            "required": "Email is required.",
            "validator_failed": "Email must be less than 130 characters.",
        },
    )
    _password = fields.String(
        load_only=True,
        required=True,
        error_messages={"required": "Password is required."},
    )
    bio = fields.String()
    location = fields.String()
    profile_image = fields.String()
    created_at = fields.DateTime()

    @validates("full_name")
    def validate_full_name(self, value):
        if value and len(value) <= 150:
            return value
        raise ValueError("Full name must be between 1 and 150 characters.")

    @validates("email")
    def validate_email(self, value):
        if value and len(value) <= 130:
            return value
        raise ValueError("Email must be less than 130 characters.")
