from flask import request
from flask_restful import Resource
import flask_restful
from main.services.auth import AuthService
from main.services.user import UserService

auth_service = AuthService()
user_service = UserService()

class AuthLogin(Resource):
    def post(self):
        if not auth_service.login(data=request.json):
            flask_restful.abort(401)
        return user_service.get(email=request.json['email'])
    
class AuthSignUp(Resource):
    def post(self):
        return auth_service.signup(data=request.json)