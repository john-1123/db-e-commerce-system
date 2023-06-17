from flask import request
from flask_restful import Resource
import flask_restful
from main.services.auth import AuthService
from main.services.user import UserService

auth_service = AuthService()
user_service = UserService()

class AuthLogin(Resource):
    def post(self):
        user = auth_service.login(data=request.json)
        if not user:
            flask_restful.abort(401)
        return user
    
class AuthSignUp(Resource):
    def post(self):
        user = auth_service.signup(data=request.json)
        if not user:
            flask_restful.abort(401)
        return user