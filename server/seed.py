#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from config import db
from data import create_users, create_artworks
from models.user import User
from models.artwork import Artwork
from models.comment import Comment
from models.like import Like
from models.follow import Follow

fake = Faker()

def create_likes(users, artworks):
    likes = []
    for _ in range(50):
        user_id = rc([user.id for user in users])
        artwork_id = rc([artwork.id for artwork in artworks])

        # Check if the like already exists
        if not any(like.user_id == user_id and like.artwork_id == artwork_id for like in likes):
            l = Like(user_id=user_id, artwork_id=artwork_id)
            likes.append(l)

    return likes

def create_comments(users, artworks):
    artwork_comments = [
    "This piece is truly captivating!",
    "I love the use of colors in this artwork.",
    "The details in this piece are incredible.",
    "A masterpiece that speaks to the soul.",
    "The artist's creativity knows no bounds.",
    "This artwork evokes a sense of wonder and awe.",
    "Absolutely stunning! I can't look away.",
    "The composition in this piece is outstanding.",
    "Such a thought-provoking work of art.",
    "I feel a deep connection to this artwork."
    ]
    comments = []
    for _ in range(50):
        c = Comment(
            user_id=rc([user.id for user in users]),
            artwork_id=rc([artwork.id for artwork in artworks]),
            content=rc(artwork_comments)
        )
        comments.append(c)

    return comments

def create_follows(users):
    follows = []
    for _ in range(35):
        follower = rc([user.id for user in users])
        following = rc([user.id for user in users])
        
        while follower == following:
            following = rc([user.id for user in users])

        f = Follow(
            follower_id=follower,
            following_id=following
        )
        follows.append(f)

    return follows

if __name__ == '__main__':
    
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        
        print("Clearing db...")
        User.query.delete()
        Artwork.query.delete()
        Like.query.delete()
        Comment.query.delete()
        Follow.query.delete()
        
        print("Creating tables...")
        db.create_all()

        print("Seeding users...")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        print("Seeding artworks...")
        artworks = create_artworks()
        db.session.add_all(artworks)
        db.session.commit()
        
        print("Seeding likes...")
        likes = create_likes(users, artworks)
        db.session.add_all(likes)
        db.session.commit()
        
        print("Seeding comments...")
        comments = create_comments(users, artworks)
        db.session.add_all(comments)
        db.session.commit()
        
        print("Seeding follows...")
        follows = create_follows(users)
        db.session.add_all(follows)
        db.session.commit()
        
        print("Seeding complete!")