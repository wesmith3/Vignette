from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from . import validates, re
from config import flask_bcrypt


class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    _password = db.Column(db.String, nullable=False)
    bio = db.Column(db.String)
    location = db.Column(db.String)
    profile_image = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Relationships
    artworks = db.relationship(
        "Artwork", back_populates="user", cascade="all, delete-orphan"
    )
    likes = db.relationship("Like", back_populates="user", cascade="all, delete-orphan")
    comments = db.relationship(
        "Comment", back_populates="user", cascade="all, delete-orphan"
    )
    followers = db.relationship(
        "Follow",
        foreign_keys="Follow.following_id",
        back_populates="following",
        cascade="all, delete-orphan",
    )
    following = db.relationship(
        "Follow",
        foreign_keys="Follow.follower_id",
        back_populates="follower",
        cascade="all, delete-orphan",
    )
    buyer_transactions = db.relationship(
        "Transaction", foreign_keys="Transaction.buyer_id", back_populates="buyer", cascade="all, delete-orphan"
    )
    # Serialization
    serialize_only = (
        "id",
        "full_name",
        "username",
        "email",
        "bio",
        "location",
        "profile_image",
        "artworks.id",
        "artworks.title",
        "artworks.image",
        "artworks.description",
        "artworks.tags",
        "likes.artwork_id",
        "comments.id",
        "comments.artwork_id",
        "comments.content",
        "followers",
        "following",
        "-followers.user",
        "-following.user",
        "-followers.follower",
        "-followers.following",
        "-followers.following_id",
        "-following.follower",
        "-following.following",
        "-following.follower_id",
    )

    @hybrid_property
    def password(self):
        raise AttributeError("Passwords are private")

    @password.setter
    def password(self, new_password):
        pw_hash = flask_bcrypt.generate_password_hash(new_password).decode("utf-8")
        self._password = pw_hash

    def verify(self, password_to_be_checked):
        return flask_bcrypt.check_password_hash(self._password, password_to_be_checked)

    def verify_jwt(self, jwt_to_be_checked):
        return self.jwt == jwt_to_be_checked

    # Validations
    @validates("full_name")
    def full_name_validation(self, k, full_name):
        if full_name and len(full_name) <= 150:
            return full_name
        else:
            raise ValueError("Full_name has to be less than 150 chars and not empty")

    @validates("email")
    def email_validation(self, k, email):
        if email and len(email) <= 130:
            return email
        else:
            raise ValueError("Full_name has to be less than 130 chars and not empty")
