from flask import request
from flask_restful import Resource
from main.services.order_table import OrderService

service = OrderService()

class GetOrder(Resource):
    def get(self):
        return service.get(data=request.json)

class CreateOrder(Resource):
    def post(self):
        return service.create(data=request.json)

# class UpdateOrder(Resource):
#     def put(self):
#         return service.update(data=request.json)

class DeleteOrder(Resource):
    def delete(self):
        return service.delete(data=request.json)
    
class GetAllOrderByMarket(Resource):
    def get(self):
        return service.get_all_order_by_market(data=request.json) ### 改request.

class GetAllOrderByMember(Resource):
    def get(self):
        return service.get_all_order_by_member(data=request.json)