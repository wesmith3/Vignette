from . import fields
from models.tag import Tag
from models.artwork import Artwork
# from .artwork_schema import ArtworkSchema
from config import ma


class TagSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tag
        load_instance = True

    id = fields.Integer(dump_only=True)
    keyword = fields.String(
        required=True,
        validate=lambda kw: Tag.validate_keyword(kw),
        error_messages={
            "required": "Keyword is required.",
            "validator_failed": "Keyword must be between 1 and 50 characters.",
        },
    )
    artwork_id = fields.Integer(
        required=True,
        validate=lambda artwork_id: Tag.validate_artwork_id(artwork_id),
        error_messages={"required": "Artwork ID is required."},
    )
    created_at = fields.DateTime(dump_only=True)
    
    # artwork = fields.Nested("ArtworkSchema", exclude=("tags",), dump_only=True)

    @staticmethod
    def validate_keyword(keyword):
        if keyword and 1 <= len(keyword) <= 50:
            return keyword
        raise ValueError("Keyword must be between 1 and 50 characters.")

    @staticmethod
    def validate_artwork_id(artwork_id):
        if artwork_id and Artwork.query.get(artwork_id):
            return artwork_id
        raise ValueError("Artwork ID must be a valid artwork.")
