from config import db
from sqlalchemy_serializer import SerializerMixin
from .user import User
from .artwork import Artwork
from . import validates, re

class Comment(db.Model, SerializerMixin):
    __tablename__="comments"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    artwork_id = db.Column(db.Integer, db.ForeignKey("artworks.id"))
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=(db.func.now()))
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
        
    #Relationships
    user = db.relationship("User", back_populates="comments")
    artwork = db.relationship("Artwork", back_populates="comments")
    
    #Serialization
    # serialize_rules=("-user",)
    serialize_only=(
        "id",
        "user_id",
        "artwork_id",
        "content",
        "created_at",
        "updated_at"
        )
    
    #Validations
    @validates('user_id')
    def user_id_validation(self, k, user_id):
        if user_id and db.session.get(User, user_id):
            return user_id
        else:
            raise ValueError('User id must be a valid user')
    
    @validates('artwork_id')
    def artwork_id_validation(self, k, artwork_id):
        if artwork_id and db.session.get(Artwork, artwork_id):
            return artwork_id
        else:
            raise ValueError('Artwork id must be a valid user')
        
    @validates('content')
    def content_validation(self, k, content):
        if content and (1 <= len(content) <= 150):
            return content
        else:
            raise ValueError('Content must be between 1 and 150 chars and not empty')
