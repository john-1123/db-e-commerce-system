import datetime

from main.models._db import save
from main.models.user import User
from main.schemas.user import UserSchema


class AuthService:
    def __init__(self):
        self.user_schema = UserSchema()

    def login(self, data):
        user = User.query.filter_by(email=data['email']).first()
        if not user or not user.verify(data['password']):
            return None
        return self.user_schema.jsonify(user)
    
    def signup(self, data):
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
        else:
            return None