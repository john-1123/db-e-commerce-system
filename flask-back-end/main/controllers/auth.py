from flask import request
from flask_restful import Resource
import flask_restful
from main.services.auth import AuthService

service = AuthService()

class AuthLogin(Resource):
    def post(self):
        if not service.login(data=request.json):
            flask_restful.abort(401)
        return True
    
class AuthSignUp(Resource):
    def post(self):
        return service.signup(data=request.json)