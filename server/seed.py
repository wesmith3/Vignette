#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Artwork, Like, Comment, Follow

fake = Faker()
        
def create_users():
    users = []
    # Artist Instances
    a1 = User(
        full_name= "Leonardo da Vinci",
        username= "leo_da_vinci",
        email= "leo_da_vinci@example.com",
        _password= "password123",
        bio= "Italian Renaissance polymath",
        location= "Vinci, Italy",
        profile_image= "leonardo.jpg"
    )
    a2 = User(
        full_name= "Vincent van Gogh",
        username= "vincent_van_gogh",
        email= "vincent_van_gogh@example.com",
        _password= "password456",
        bio= "Post-Impressionist painter",
        location= "Zundert, Netherlands",
        profile_image= "van_gogh.jpg"
    )
    a3 = User(
        full_name= "Pablo Picasso",
        username= "pablo_picasso",
        email= "pablo_picasso@example.com",
        _password= "password789",
        bio= "Cubist artist and sculptor",
        location= "Málaga, Spain",
        profile_image= "picasso.jpg"
    )
    a4 = User(
        full_name= "Claude Monet",
        username= "claude_monet",
        email= "claude_monet@example.com",
        _password= "password112",
        bio= "Impressionist painter",
        location= "Paris, France",
        profile_image= "monet.jpg"
    )
    a5 = User(
        full_name= "Salvador Dalí",
        username= "salvador_dali",
        email= "salvador_dali@example.com",
        _password= "password131",
        bio= "Surrealist artist",
        location= "Figueres, Spain",
        profile_image= "dali.jpg"
    )
    a6 = User(
        full_name= "Michelangelo Buonarroti",
        username= "michelangelo",
        email= "michelangelo@example.com",
        _password= "password141",
        bio= "Renaissance sculptor and painter",
        location= "Caprese, Italy",
        profile_image= "michelangelo.jpg"
    )
    a7 = User(
        full_name= "Frida Kahlo",
        username= "frida_kahlo",
        email= "frida_kahlo@example.com",
        _password= "password151",
        bio= "Mexican painter known for her self-portraits",
        location= "Coyoacán, Mexico",
        profile_image= "frida_kahlo.jpg"
    )
    a8 = User(
        full_name= "Andy Warhol",
        username= "andy_warhol",
        email= "andy_warhol@example.com",
        _password= "password161",
        bio= "Pop art pioneer",
        location= "Pittsburgh, USA",
        profile_image= "warhol.jpg"
    )
    a9 = User(
        full_name= "Raphael Sanzio",
        username= "raphael_sanzio",
        email= "raphael_sanzio@example.com",
        _password= "password171",
        bio= "High Renaissance painter",
        location= "Urbino, Italy",
        profile_image= "raphael.jpg"
    )
    a10 = User(
        full_name= "Edvard Munch",
        username= "edvard_munch",
        email= "edvard_munch@example.com",
        _password= "password181",
        bio= "Expressionist painter",
        location= "Oslo, Norway",
        profile_image= "munch.jpg"
    )
    a11 = User(
        full_name= "Rembrandt van Rijn",
        username= "rembrandt",
        email= "rembrandt@example.com",
        _password= "password191",
        bio= "Dutch Golden Age painter",
        location= "Leiden, Netherlands",
        profile_image= "rembrandt.jpg"
    )
    a12 = User(
        full_name= "Jackson Pollock",
        username= "jackson_pollock",
        email= "jackson_pollock@example.com",
        _password= "password201",
        bio= "Abstract expressionist painter",
        location= "Cody, USA",
        profile_image= "pollock.jpg"
    )
    users.extend([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12])

    return users

def create_artworks(users):
    artworks = []
    a1 = Artwork(
        user_id=1,
        title = "Mona Lisa",
        description = "Portrait of Lisa Gherardini, wife of Francesco del Giocondo",
        image = "mona_lisa.jpg",
        tags = "portrait, woman, smile, Renaissance"
    )
    a2 = Artwork(
        user_id=1,
        title = "The Last Supper",
        description = "Depiction of the last meal of Jesus with his disciples",
        image = "last_supper.jpg",
        tags = "religious, Jesus, disciples, Renaissance"

    )
    a3 = Artwork(
        user_id=1,
        title = "Vitruvian Man",
        description = "Study of the proportions of the human body according to Vitruvius",
        image = "vitruvian_man.jpg",
        tags = "anatomy, human body, proportions, Renaissance"
    )
    a4 = Artwork(
        user_id=1,
        title = "Annunciation",
        description = "Archangel Gabriel announcing to the Virgin Mary that she will conceive Jesus",
        image = "annunciation.jpg",
        tags = "religious, Annunciation, angel, Virgin Mary, Renaissance",

    )
    a5 = Artwork(
        user_id=1,
        title = "Lady with an Ermine",
        description = "Portrait of Cecilia Gallerani holding an ermine",
        image = "lady_with_an_ermine.jpg",
        tags = "portrait, woman, ermine, Renaissance"

    )
    artworks.extend([a1,a2,a3,a4,a5])
    return artworks

def create_likes(users, artworks):
    likes = []
    for _ in range(50):
        l = Like(
            user_id=rc([user.id for user in users]),
            artwork_id=rc([artwork.id for artwork in artworks])
        )
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
        artworks = create_artworks(users)
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