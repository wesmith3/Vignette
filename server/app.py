#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, Flask, make_response
from flask_restful import Resource
from models import User, Artwork, Like, Comment, Follow
import json
import flask_bcrypt

# Local imports
from config import app, db, api
# Add your model imports

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
            
            new_artwork = Artwork(
                user_id = id,
                title = data["title"],
                description = data["description"],
                image = data["image"],
                tags = data["tags"]
            )

            db.session.add(new_artwork)
            db.session.commit()
            return make_response(new_artwork.to_dict(rules=("-user",)), 201)
        except (ValueError, AttributeError, TypeError) as e:
            db.session.rollback()
            return make_response(
                {"errors": [str(e)]}, 400
            )
    
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
            return make_response(new_like.to_dict(), 201)
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
        followers = Follow.query.filter_by(following_id=id).all()

        users_following = [follow.to_dict() for follow in followers]

        return users_following, 200
    
api.add_resource(FollowersByUserId, "/users/<int:id>/followers")

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

