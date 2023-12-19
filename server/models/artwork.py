from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.schema import UniqueConstraint
from .user import User
import stripe
import os
from . import validates, re


class Artwork(db.Model, SerializerMixin):
    __tablename__ = "artworks"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    image = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stripe_product_id = db.Column(db.String)
    stripe_price_id = db.Column(db.String)
    preview = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    def __init__(self, *args, **kwargs):
        super(Artwork, self).__init__(*args, **kwargs)
        self.create_stripe_product_and_price()

    __table_args__ = (UniqueConstraint("user_id", "title", name="unique_user_title"),)
    
    def create_stripe_product_and_price(self):
        stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

        # Check if Stripe IDs already exist
        if not self.stripe_product_id or not self.stripe_price_id:
            # Create product on Stripe
            stripe_product = stripe.Product.create(
                name=self.title,
                description=self.description,
                type="service",
            )

            # Create price on Stripe
            stripe_price = stripe.Price.create(
                product=stripe_product.id,
                unit_amount=int(self.price * 100),  # Convert to cents
                currency="usd",
            )

            # Update artwork record with Stripe IDs
            self.stripe_product_id = stripe_product.id
            self.stripe_price_id = stripe_price.id

            db.session.commit()

    # Relationships
    user = db.relationship("User", back_populates="artworks")
    likes = db.relationship(
        "Like", back_populates="artwork", cascade="all, delete-orphan"
    )
    comments = db.relationship(
        "Comment", back_populates="artwork", cascade="all, delete-orphan"
    )
    tags = db.relationship(
        "Tag", back_populates="artworks", cascade="all, delete-orphan"
    )
    transactions = db.relationship(
        "Transaction", back_populates="artwork", cascade="all, delete-orphan"
    )

    # Serialization
    serialize_rules = ("-user.artworks", "-likes.artwork", "-comments.artwork")

    # Validations
    @validates("user_id")
    def user_id_validation(self, k, user_id):
        if user_id and db.session.get(User, user_id):
            return user_id
        else:
            raise ValueError("User id must be a valid user")

    @validates("title")
    def title_validation(self, key, title):
        if title and (1 <= len(title) <= 130):
            return title
        else:
            raise ValueError("Title must be between 1 and 130 chars and not empty")

    @validates("description")
    def description_length_validation(self, k, description):
        if len(description) <= 300:
            return description
        else:
            raise ValueError("Description cannot be longer than 300 chars")
