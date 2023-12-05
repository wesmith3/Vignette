#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Artwork, Like, Comment, Follow

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        
        def create_users():
            users = []
            for _ in range(10):
                # pw_hash = flask_bcrypt.generate_password_hash("password").decode("utf-8")
                c = User(
                    full_name=fake.name(),
                    username=fake.username(),
                    email=fake.email(),
                    created_at= fake.date_time()
                )
                c.password = "password"
                users.append(c)

            return users
