from config import db
from sqlalchemy_serializer import SerializerMixin
from .artwork import Artwork
from . import validates, re

class Tag(db.Model, SerializerMixin):
    __tablename__="tags"
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String, nullable=False)
    artwork_id = db.Column(db.Integer, db.ForeignKey("artworks.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    #Relationship
    artworks = db.relationship("Artwork", back_populates="tags")
    
    #Serialization
    serialize_only = (
        "id",
        "keyword",
        "artwork_id"
    )
    
    #Validations
    @validates('artwork_id')
    def artwork_id_validation(self, k, artwork_id):
        if artwork_id and db.session.get(Artwork, artwork_id):
            return artwork_id
        else:
            raise ValueError('Artwork id must be a valid artwork')
        
    @validates('keyword')
    def content_validation(self, k, keyword):
        if keyword and (1 <= len(keyword) <= 50):
            return keyword
        else:
            raise ValueError('Keyword must be between 1 and 50 chars and not empty')
   