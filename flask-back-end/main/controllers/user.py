from flask import request
from flask_restful import Resource
from main.services.user import UserService

service = UserService()

class GetAllUser(Resource):
    def get(self):
        return service.get_all()

class GetUser(Resource):
    def get(self, id):
        return service.get(user_id=id)

class PostUser(Resource):
    def post(self):
        return service.create(data=request.json)

class UpdateUser(Resource):
    def put(self, id):
        return service.update(user_id=id, data=request.json)

class DeleteUser(Resource):
    def delete(self, id):
        return service.delete(user_id=id)