from flask import request
from flask_restful import Resource
from main.services.auth import AuthService

service = AuthService()

class AuthLogin(Resource):
    def post(self):
        return service.login(data=request.json)
    
class AuthSignUp(Resource):
    def post(self):
        return service.signup(data=request.json)