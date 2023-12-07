from config import db
from sqlalchemy_serializer import SerializerMixin
from .user import User
from .artwork import Artwork
from . import validates, re

class Like(db.Model, SerializerMixin):
    __tablename__="likes"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    artwork_id = db.Column(db.Integer, db.ForeignKey("artworks.id"), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
        
    #Relationships
    user = db.relationship("User", back_populates="likes")
    artwork = db.relationship("Artwork", back_populates="likes")
    
    #Serialization
    serialize_only=(
        "user_id",
        "artwork_id"
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
            raise ValueError('Artwork id must be connected to a valid artwork')
