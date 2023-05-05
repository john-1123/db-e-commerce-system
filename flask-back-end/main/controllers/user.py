from flask import request
from flask_restful import Resource
from main.services.user import get_all_users, get_user, create_user, update_user, delete_user

class GetAllUser(Resource):
    def get(self):
        return get_all_users()

class GetUser(Resource):
    def get(self, id):
        return get_user(user_id=id)

class PostUser(Resource):
    def post(self):
        return create_user(data=request.json)

class UpdateUser(Resource):
    def put(self, id):
        return update_user(user_id=id, data=request.json)

class DeleteUser(Resource):
    def delete(self, id):
        return delete_user(user_id=id)