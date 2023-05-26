from main.models._db import save, delete
from flask import jsonify
from main.models.user import User
from main.schemas.user import UserSchema
import datetime

class UserService:
    def __init__(self):
        self.user_schema = UserSchema()
        self.users_schema = UserSchema(many=True)

    def get_all(self):
        users = User.query.all()
        return jsonify(self.users_schema.dump(users))

    def get(self, email):
        user = User.query.filter_by(email=email).first()
        return self.user_schema.jsonify(user)

    def create(self, data):
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            new_user = User(
                email = data['email'],
                password = data['password'],
                username = data['username'],
                address = data['address'],
                phone = data['phone'],
                registered_on = datetime.datetime.now()
            )
            save(new_user)
            return self.user_schema.jsonify(new_user)

    def update(self, user_id, data):
        user = User.query.get(user_id)
        if user:
            user.email = data['email'],
            user.password = data['password'],
            user.username = data['username'],
            user.address = data['address'],
            user.phone = data['phone'],
            save(user)
            return self.user_schema.jsonify(user)

    def delete(self, user_id):
        user = User.query.get(user_id)
        if user:
            delete(user)
            return user_id
