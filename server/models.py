from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    bio = db.Column(db.String)
    location = db.Column(db.String)
    username = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=(db.func.now()))
    updated_at = db.Column(db.DateTime, onupdate=(db.func.now()))
    
    #Relationships
    
    
    #Serialization


class Artwork(db.Model, SerializerMixin):
    __tablename__='artworks'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.String)
    tags = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=(db.func.now()))
    updated_at = db.Column(db.DateTime, onupdate=(db.func.now()))
        
    #Relationships
    
    
    #Serialization


class Like(db.Model, SerializerMixin):
    __tablename__='likes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    artwork_id = db.Column(db.Integer, db.ForeignKey('artworks.id'))
    created_at = db.Column(db.DateTime, server_default=(db.func.now()))
    updated_at = db.Column(db.DateTime, onupdate=(db.func.now()))
        
    #Relationships
    
    
    #Serialization


class Comment(db.Model, SerializerMixin):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    artwork_id = db.Column(db.Integer, db.ForeignKey('artworks.id'))
    created_at = db.Column(db.DateTime, server_default=(db.func.now()))
    updated_at = db.Column(db.DateTime, onupdate=(db.func.now()))
        
    #Relationships
    
    
    #Serialization


class Follow(db.Model, SerializerMixin):
    __tablename__='follows'
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    following_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, server_default=(db.func.now()))
    updated_at = db.Column(db.DateTime, onupdate=(db.func.now()))
        
    #Relationships
    
    
    #Serialization

