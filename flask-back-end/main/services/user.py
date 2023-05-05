from main.models._db import save, delete
from flask import jsonify
from main.models.user import User
from main.schemas.user import UserSchema
import datetime

user_schema = UserSchema()
users_schema = UserSchema(many=True)


def get_all_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users))

def get_user(user_id):
    user = User.query.get(user_id)
    return user_schema.jsonify(user)

def create_user(data):
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
        return user_schema.jsonify(new_user)

def update_user(user_id, data):
    user = User.query.get(user_id)
    if user:
        user.email = data['email'],
        user.password = data['password'],
        user.username = data['username'],
        user.address = data['address'],
        user.phone = data['phone'],
        save(user)
        return user_schema.jsonify(user)

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        delete(user)
        return user_id


