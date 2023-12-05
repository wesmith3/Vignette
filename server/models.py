from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.ext.hybrid import hybrid_property
import bcrypt
import re

from config import db

# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)
    bio = db.Column(db.String)
    location = db.Column(db.String)
    profile_image = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    #Relationships
    artworks = db.relationship("Artwork", back_populates="user", cascade="all, delete-orphan")
    likes = db.relationship("Like", back_populates="user", cascade="all, delete-orphan")
    comments = db.relationship("Comment", back_populates="user", cascade="all, delete-orphan")
    followers = db.relationship("Follow", foreign_keys="Follow.following_id", back_populates="following", cascade="all, delete-orphan")
    following = db.relationship("Follow", foreign_keys="Follow.follower_id", back_populates="follower", cascade="all, delete-orphan")
    
    #Serialization
    serialize_rules=("-password", "-artworks.user", "-likes.user", "-comments.user")
    
    
    @hybrid_property
    def password(self):
        raise AttributeError('No looking at the password')

    @password.setter
    def password(self, password):
        if password and  5<= len(str(password)) <= 75:
            self._password_hash = bcrypt.hashpw(password=password.encode('utf-8'),salt=bcrypt.gensalt())
        else:
            raise ValueError('Password must be longer than 5 characters and less than 75')
       

    def authenticate(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self._password_hash)
    
    #Validations
    @validates('full_name')
    def full_name_validation(self, k, full_name):
        if full_name and len(full_name) <=50:
            return full_name
        else:
            raise ValueError('Full_name has to be less than 50 chars and not empty')
        
    @validates('username')
    def username_validation(self, key, username):
        if username and (5 <= len(str(username)) <= 12):
            if re.match('^[a-zA-Z0-9_]+$', str(username)):
                return str(username)
            else:
                raise ValueError('Name can only contain letters, numbers, and underscores')
        else:
            raise ValueError('Username must be between 5 and 12 characters')
        
    @validates('email')
    def email_validation(self, k, email):
        if email and len(email) <=30:
            return email
        else:
            raise ValueError('Full_name has to be less than 30 chars and not empty')

class Artwork(db.Model, SerializerMixin):
    __tablename__="artworks"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    image = db.Column(db.String, nullable=False)
    tags = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    __table_args__ = (
        UniqueConstraint('user_id', 'title', name='unique_user_title'),
    )
        
    #Relationships
    user = db.relationship("User", back_populates="artworks")
    likes = db.relationship("Like", back_populates="artwork", cascade="all, delete-orphan")
    comments = db.relationship("Comment", back_populates="artwork", cascade="all, delete-orphan")
    
    #Serialization
    serialize_rules=("-user.artworks", "-likes.artwork", "-comments.artwork")
    
    #Validations
    @validates('user_id')
    def user_id_validation(self, k, user_id):
        if user_id and db.session.get(User, user_id):
            return user_id
        else:
            raise ValueError('User id must be a valid user')
        
    @validates('image')
    def image_validation(self, k, image):
        if image:
            return image
        else:
            raise ValueError('Image cannot be empty')
        
    @validates('title')
    def title_validation(self, key, title):
        if title and (1 <= len(title) <= 30):
            return title
        else:
            raise ValueError('Title must be between 1 and 30 chars and not empty')
        
    @validates('description')
    def description_length_validation(self, k, description):
        if len(description) <= 300:
            return description
        else:
            raise ValueError('Description cannot be longer than 300 chars')

class Like(db.Model, SerializerMixin):
    __tablename__="likes"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    artwork_id = db.Column(db.Integer, db.ForeignKey("artworks.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
        
    #Relationships
    user = db.relationship("User", back_populates="likes")
    artwork = db.relationship("Artwork", back_populates="likes")
    
    #Serialization
    serialize_rules=("-user.likes", "-artwork.likes")
    
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
    serialize_rules=("-user.comments", "-artwork.comments")
    
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
        if content and (1 <= len(content) <= 30):
            return content
        else:
            raise ValueError('Content must be between 1 and 50 chars and not empty')
    
class Follow(db.Model, SerializerMixin):
    __tablename__="follows"
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    following_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
        
    #Relationships
    follower = db.relationship('User', foreign_keys=[follower_id], back_populates='following')
    following = db.relationship('User', foreign_keys=[following_id], back_populates='followers')
    
    #Serialization
    serialize_rules=("-follower.following", "-following.followers")
    
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
