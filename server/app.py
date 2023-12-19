#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, Flask, make_response, session, redirect
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_
import stripe
from flask_restful import Resource
from models.user import User
from schemas.user_schema import UserSchema
from models.artwork import Artwork
from models.like import Like
from models.comment import Comment
from models.follow import Follow
from models.tag import Tag
from models.transaction import Transaction
import os
import json
import ipdb
import flask_bcrypt
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    unset_access_cookies,
    unset_refresh_cookies,
    jwt_required,
    current_user,
    get_jwt_identity,
)

# Local imports
from config import app, db, api, jwt
# Add your model imports
user_schema = UserSchema(session=db.session)
YOUR_DOMAIN = 'http://localhost:3000'
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")
endpoint_secret = os.environ.get('ENDPOINT_SECRET')

def create_stripe_price(artwork_id, price_in_cents):
        artwork = db.session.get(Artwork, artwork_id)
        try:
            product_id = artwork.stripe_product_id

            price = stripe.Price.create(
                product=product_id,
                unit_amount=price_in_cents,
                currency='usd',
            )

            return price
        except stripe.error.StripeError as e:
            print(f"Error creating Stripe price: {e}")
            raise

class Users(Resource):
    def get(self):
        try:
            u_list = []
            users = User.query
            for user in users:
                u_list.append(user.to_dict(rules=('-password',)))
            return make_response(u_list, 200)
        except (ValueError, AttributeError, TypeError) as e:
            return make_response(
                {"errors": [str(e)]}, 400
            )
    
    def post(self):
        try:
            data = json.loads(request.data)
            pw_hash = flask_bcrypt.generate_password_hash(data["password"])
            
            new_user = User(
                full_name = data["full_name"],
                username = data["username"],
                email = data["email"],
                _password = pw_hash,
                bio = data["bio"],
                location = data["location"],
                profile_image = data["profile_image"]
            )

            db.session.add(new_user)
            db.session.commit()
            return make_response(new_user.to_dict(rules=("-password",)), 201)
        except (ValueError, AttributeError, TypeError) as e:
            db.session.rollback()
            return make_response(
                {"errors": [str(e)]}, 400
            )

api.add_resource(Users, "/users")

class UserById(Resource):
    def get(self, id):
        try:
            user = db.session.get(User, id)
            if user:
                return user.to_dict(rules=('-password',))
            else:
                return make_response(
                    {"errors": "User Not Found"}, 404
                )
        except (ValueError, AttributeError, TypeError) as e:
            return make_response(
                {"errors": [str(e)]}, 400
            )
            
    def patch(self, id):
        try:
            user = db.session.get(User, id)
            if user:
                data = json.loads(request.data)
                for attr in data:
                    setattr(user, attr, data[attr])
                db.session.add(user)
                db.session.commit()
                return user.to_dict(), 200
            else:
                return make_response(
                    {"errors": "Update unsuccessful"}, 400
                )
        except (ValueError, AttributeError, TypeError) as e:
            db.session.rollback()
            return make_response(
                {"errors": [str(e)]}, 400
            )
    
    def delete(self,id):
        try:
            user = db.session.get(User, id)
            if user:
                db.session.delete(user)
                db.session.commit()
                return {}, 204
            else:
                return make_response(
                    {"errors": "Delete unsuccessful"}, 400
                )
        except (ValueError, AttributeError, TypeError) as e:
            db.session.rollback()
            return make_response(
                {"errors": [str(e)]}, 400
            )

api.add_resource(UserById, "/users/<int:id>")

class Artworks(Resource):
    def get(self):
        try:
            a_list = []
            artworks = Artwork.query
            for artwork in artworks:
                a_list.append(artwork.to_dict())
            return make_response(a_list, 200)
        except (ValueError, AttributeError, TypeError) as e:
            return make_response(
                {"errors": [str(e)]}, 400
            )

api.add_resource(Artworks, "/artworks")

class ArtworksByUserId(Resource):
    def get(self, id):
        try:
            a_list = []
            user = db.session.get(User, id).to_dict()
            user_id = user['id']
            artworks = Artwork.query.filter(Artwork.user_id==user_id)
            for artwork in artworks:
                a_list.append(artwork.to_dict())
            return a_list, 200
        except (ValueError, AttributeError, TypeError) as e:
            return make_response(
                {"errors": [str(e)]}
            )
    
    def post(self, id):
        try:
            data = json.loads(request.data)
            tags_data = data.get("tags", [])

            # Create a new artwork
            new_artwork = Artwork(
                user_id=id,
                title=data["title"],
                description=data["description"],
                image=data["image"],
                price=data["price"],  # Assuming "price" is part of the request
                preview=data["preview"],  # Assuming "preview" is part of the request
            )

            # Associate existing or newly created tags with the artwork
            for tag_data in tags_data:
                tag = Tag.query.filter_by(keyword=tag_data).first()
                if tag is None:
                    tag = Tag(keyword=tag_data)
                    db.session.add(tag)

                new_artwork.tags.append(tag)

            db.session.add(new_artwork)
            db.session.commit()

            return make_response(new_artwork.to_dict(rules=("-user",)), 201)
        except (ValueError, AttributeError, TypeError) as e:
            db.session.rollback()
            return make_response({"errors": [str(e)]}, 400)

api.add_resource(ArtworksByUserId, "/users/<int:id>/artworks")
    
class ArtworkById(Resource):
    def get(self, id):
        try:
            artwork = db.session.get(Artwork, id)
            if artwork:
                return make_response(
                    artwork.to_dict(
                        rules=(
                            "-user.comments",
                            "-user.followers",
                            "-user.following",
                            "-user.likes"
                            )
                        ), 200)
            else:
                return make_response(
                    {"errors": "Artwork Not Found"}, 404
                )
        except (ValueError, AttributeError, TypeError) as e:
            return make_response(
                {"errors": [str(e)]}, 400
            )
    
    
        
    def patch(self, id):
        try:
            artwork = db.session.get(Artwork, id)
            if artwork:
                data = json.loads(request.data)
                for attr in data:
                    setattr(artwork, attr, data[attr])
                db.session.add(artwork)
                db.session.commit()

                new_price = create_stripe_price(artwork.id, artwork.price)

                artwork.stripe_price_id = new_price['id']
                db.session.commit()

                return make_response(
                    artwork.to_dict(
                        rules=(
                            "-user.comments",
                            "-user.following",
                            "-user.followers",
                            "-user.likes"
                        )
                    ), 200)
            else:
                return make_response(
                    {"errors": "Update unsuccessful"}, 400
                )
        except (ValueError, AttributeError, TypeError) as e:
            db.session.rollback()
            return make_response(
                {"errors": [str(e)]}, 400
            )

    
    def delete(self, id):
        try:
            artwork = db.session.get(Artwork, id)
            if artwork:
                db.session.delete(artwork)
                db.session.commit()
                return make_response({}, 204)
            else:
                return make_response(
                    {"errors": "Delete unsuccessful"}, 400
                )
        except (ValueError, AttributeError, TypeError) as e:
            db.session.rollback()
            return make_response(
                {"errors": [str(e)]}, 400
            )
    
api.add_resource(ArtworkById, "/artworks/<int:id>")
    
class CommentsByArtworkId(Resource):
    def get(self, id):
        try:
            c_list = []
            artwork = db.session.get(Artwork, id).to_dict()
            artwork_id = artwork['id']
            comments = Comment.query.filter(Comment.artwork_id==artwork_id)
            for comment in comments:
                c_list.append(comment.to_dict(rules=("-artwork_id",)))
            return c_list, 200
        except (ValueError, AttributeError, TypeError) as e:
            return make_response(
                {"errors": [str(e)]}
            )
            
    def post(self, id):
        try:
            data = json.loads(request.data)
            
            new_comment = Comment(
                user_id = data["user_id"],
                artwork_id = id,
                content = data["content"]
            )

            db.session.add(new_comment)
            db.session.commit()
            return make_response(new_comment.to_dict(), 201)
        except (ValueError, AttributeError, TypeError) as e:
            db.session.rollback()
            return make_response(
                {"errors": [str(e)]}, 400
            )
        
api.add_resource(CommentsByArtworkId, "/artworks/<int:id>/comments")

class CommentById(Resource):
    def get(self, id):
        try:
            comment = db.session.get(Comment, id)
            if comment:
                return make_response(comment.to_dict(), 200)
            else:
                return make_response(
                    {"errors": "Comment Not Found"}, 404
                )
        except (ValueError, AttributeError, TypeError) as e:
            return make_response(
                {"errors": [str(e)]}, 400
            )
    
    def patch(self, id):
        try:
            comment = db.session.get(Comment, id)
            if comment:
                data = json.loads(request.data)
                for attr in data:
                    setattr(comment, attr, data[attr])
                db.session.add(comment)
                db.session.commit()
                return make_response(comment.to_dict(), 200)
            else:
                return make_response(
                    {"errors": "Update unsuccessful"}, 400
                )
        except (ValueError, AttributeError, TypeError) as e:
            db.session.rollback()
            return make_response(
                {"errors": [str(e)]}, 400
            )
    
    def delete(self, id):
        try:
            comment = db.session.get(Comment, id)
            if comment:
                db.session.delete(comment)
                db.session.commit()
                return make_response({}, 204)
            else:
                return make_response(
                    {"errors": "Delete unsuccessful"}, 400
                )
        except (ValueError, AttributeError, TypeError) as e:
            db.session.rollback()
            return make_response(
                {"errors": [str(e)]}, 400
            )
    
api.add_resource(CommentById, "/comments/<int:id>")
    
class LikesByArtworkId(Resource):
    def get(self, id):
        try:
            l_list = []
            artwork = db.session.get(Artwork, id).to_dict()
            artwork_id = artwork['id']
            likes = Like.query.filter(Like.artwork_id==artwork_id)
            for like in likes:
                l_list.append(like.to_dict(rules=("-artwork_id",)))
            return l_list, 200
        except (ValueError, AttributeError, TypeError) as e:
            return make_response(
                {"errors": [str(e)]}
            )
            
    def post(self, id):
        try:
            data = json.loads(request.data)
            new_like = Like(
                user_id = data["user_id"],
                artwork_id = id
            )

            db.session.add(new_like)
            db.session.commit()
            return make_response(new_like.to_dict(rules=("-artwork_id",)), 201)
        except (ValueError, AttributeError, TypeError) as e:
            db.session.rollback()
            return make_response(
                {"errors": [str(e)]}, 400
            )
            
    def delete(self, id):
        try:
            data = json.loads(request.data)
            user_id = data.get("user_id")
            
            if not user_id:
                return make_response(
                    {"errors": ["user_id is required in the request body"]}, 400
                )

            like = Like.query.filter_by(artwork_id=id, user_id=user_id).first()

            if like:
                db.session.delete(like)
                db.session.commit()
                return make_response({}, 204)
            else:
                return make_response(
                    {"errors": "Delete unsuccessful. Like not found for the specified user and artwork"}, 400
                )
        except (ValueError, AttributeError, TypeError) as e:
            db.session.rollback()
            return make_response(
                {"errors": [str(e)]}, 400
            )
        
api.add_resource(LikesByArtworkId, "/artworks/<int:id>/likes")

class LikeById(Resource):
    def get(self, id):
        try:
            like = db.session.get(Like, id)
            if like:
                return make_response(like.to_dict(), 200)
            else:
                return make_response(
                    {"errors": "Like Not Found"}, 404
                )
        except (ValueError, AttributeError, TypeError) as e:
            return make_response(
                {"errors": [str(e)]}, 400
            )
    
    def delete(self, id):
        try:
            like = db.session.get(Like, id)
            if like:
                db.session.delete(like)
                db.session.commit()
                return make_response({}, 204)
            else:
                return make_response(
                    {"errors": "Delete unsuccessful"}, 400
                )
        except (ValueError, AttributeError, TypeError) as e:
            db.session.rollback()
            return make_response(
                {"errors": [str(e)]}, 400
            )
    
api.add_resource(LikeById, "/likes/<int:id>")

class FollowingByUserId(Resource):
    def get(self, id):
        follows = Follow.query.filter_by(follower_id=id).all()

        following_users = [follow.to_dict() for follow in follows]

        return following_users, 200
    
    def post(self, id):
        
        data = json.loads(request.data)

        if "following_id" not in data:
            return {"message": "Missing 'following_id' in the request body"}, 400

        following_id = data['following_id']

        existing_follow = Follow.query.filter_by(follower_id=id, following_id=following_id).first()

        if existing_follow:
            return {"message": "The follow relationship already exists"}, 400

        new_follow = Follow(
            follower_id=id,
            following_id=following_id
            )

        db.session.add(new_follow)
        db.session.commit()
        return new_follow.to_dict(), 201

api.add_resource(FollowingByUserId, "/users/<int:id>/following")

class DeleteFollow(Resource):
    def delete(self, id):
        data = json.loads(request.data)

        if "following_id" not in data:
            return {"message": "Missing 'following_id' in the request body"}, 400

        following_id = data['following_id']

        existing_follow = Follow.query.filter_by(follower_id=id, following_id=following_id).first()

        if not existing_follow:
            return {"message": "The follow relationship does not exist"}, 404

        db.session.delete(existing_follow)
        db.session.commit()

        return {"message": "Successfully deleted the follow relationship"}, 200
    
api.add_resource(DeleteFollow, "/users/<int:id>/follow")
    
class FollowersByUserId(Resource):
    def get(self, id):
        followers = Follow.query.filter_by(follower_id=id).all()

        users_following = [follow.to_dict() for follow in followers]

        return users_following, 200
    
api.add_resource(FollowersByUserId, "/users/<int:id>/followers")

class TransactionsByUserId(Resource):
    def get(self, id):
        try:
            t_list = []
            user = db.session.get(User, id).to_dict()
            user_id = user['id']
            
            transactions = Transaction.query.filter(or_(Transaction.buyer_id == user_id, Transaction.seller_id == user_id))

            for transaction in transactions:
                t_list.append(transaction.to_dict())
            
            return t_list, 200

        except (ValueError, AttributeError, TypeError) as e:
            return make_response(
                {"errors": [str(e)]}
        )
    
    def post(self, id):
        try:
            data = json.loads(request.data)
            
            new_transaction = Transaction(
                buyer_id = id,
                seller_id = data["seller_id"],
                amount_paid = data["amount_paid"],
                description = data["description"],
                artwork_id = data["artwork_id"]
            )

            db.session.add(new_transaction)
            db.session.commit()
            return make_response(new_transaction.to_dict(rules=("-user",)), 201)
        except (ValueError, AttributeError, TypeError) as e:
            db.session.rollback()
            return make_response(
                {"errors": [str(e)]}, 400
            )
    
api.add_resource(TransactionsByUserId, "/users/<int:id>/transactions")
    
class Signup(Resource):
    def post(self):
        try:
            data = json.loads(request.data)
            pw_hash = flask_bcrypt.generate_password_hash(data["password"])

            new_user = User(
                full_name=data["full_name"],
                username=data["username"],
                email=data["email"],
                _password=pw_hash,
                bio=data["bio"],
                location=data["location"],
                profile_image=""
            )

            db.session.add(new_user)
            db.session.commit()

            jwt = create_access_token(identity=new_user.id)
            refresh_token = create_refresh_token(identity=new_user.id)
            serialized_user = user_schema.dump(new_user)
            response = make_response(serialized_user, 201)
            set_access_cookies(response, jwt)
            set_refresh_cookies(response, refresh_token)
            return response
        except IntegrityError as e:
            db.session.rollback()

            # Check if the error is related to a unique constraint violation
            if 'UNIQUE constraint failed: users.email' in str(e):
                return {"message": "Please choose another email."}, 400
            elif 'UNIQUE constraint failed: users.username' in str(e):
                return {"message": "Please choose another username."}, 400
            else:
                # Handle other IntegrityError cases if needed
                return {"message": "An error occurred while processing your request."}, 400

api.add_resource(Signup, "/signup")

class Login(Resource):
    def post(self):
        try:
            data = request.get_json()
            user = User.query.filter_by(email=data.get("email")).first()
            
            if user and user.verify((data.get("_password"))):
                jwt = create_access_token(identity=user.id)
                refresh_token = create_refresh_token(identity=user.id)
                
                serialized_user = user_schema.dump(user)
                response = make_response(serialized_user, 200)
                
                set_access_cookies(response, jwt)
                set_refresh_cookies(response, refresh_token)
                
                return response
            
            return {"message": "Invalid Credentials"}, 403
        except Exception as e:
            return make_response(
                {"errors": [str(e)]}
            )
        
api.add_resource(Login, "/login")

class Logout(Resource):
    def delete(self):
        # del session["user_id"]
        response = make_response({}, 204)
        unset_access_cookies(response)
        unset_refresh_cookies(response)
        return response

api.add_resource(Logout, "/logout")

class Me(Resource):
    @jwt_required()
    def get(self):
        return user_schema.dump(current_user), 200
    
api.add_resource(Me, "/me")

class Refresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        id_ = get_jwt_identity()
        response = make_response(user_schema.dump(current_user), 200)
        access_token = create_access_token(identity=id_)
        set_access_cookies(response, access_token)
        return response

api.add_resource(Refresh, "/refresh")

# Views go here!

@app.route('/create-checkout-session/<int:id>', methods=['POST'])
def create_checkout_session(id):
    artwork_to_purchase = Artwork.query.get(id)
    
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': artwork_to_purchase.stripe_price_id,
                'quantity': 1
            }
        ],
        mode='payment',
        success_url=YOUR_DOMAIN + "/success",
        cancel_url=YOUR_DOMAIN + "/cancelled"
    )
    return redirect(checkout_session.url, code=303)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.get_data()
    sig_header = request.headers.get('Stripe_Signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        raise e
    except stripe.error.SignatureVerificationError as e:
        raise e

    if event['type'] == 'checkout.session.completed':
        checkout_session = event['data']['object']
        data_for_db = Transaction()
        data_for_db.buyer_id = checkout_session.client_reference_id
        data_for_db.artwork_id = checkout_session.line_items.price.product
        if checkout_session.payment_status == 'paid':
            data_for_db.amount_paid = checkout_session.amount_total
        db.session.add(data_for_db)
        db.session.commit()
    else:
        print('Unhandled event type {}'.format(event['type']))

    return make_response(success=True)

@app.route('/')
def index():
    return '<h1>Vignette Server</h1>'

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return db.session.get(User, identity)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

