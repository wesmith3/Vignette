from config import db
from sqlalchemy_serializer import SerializerMixin
from .user import User
from .artwork import Artwork
from . import validates, re

class Follow(db.Model, SerializerMixin):
    __tablename__="follows"
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    following_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
        
    #Relationships
    follower = db.relationship('User', foreign_keys=[follower_id], back_populates='following')
    following = db.relationship('User', foreign_keys=[following_id], back_populates='followers')
    
    # #Serialization
    serialize_only=(
        "id",
        "follower_id",
        "following_id",
        "following.artworks"
    )
    
    #Validations
    @validates('follower_id')
    def follower_id_validation(self, key, follower_id):
        if follower_id and db.session.get(User, follower_id):
            return follower_id
        else:
            raise ValueError('User id must be a valid user')
    
    @validates('following_id')
    def following_id_validation(self, key, following_id):
        if following_id and db.session.get(User, following_id):
            return following_id
        else:
            raise ValueError('User id must be a valid user')
