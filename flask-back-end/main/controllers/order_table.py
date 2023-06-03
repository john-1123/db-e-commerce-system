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
    def delete(self, id):
        return service.delete(order_id=id)
    
class GetAllOrderByMarket(Resource):
    def get(self, id):
        return service.get_all_order_by_market(market_id=id) ### 改request.

class GetAllOrderByMember(Resource):
    def get(self, id):
        return service.get_all_order_by_member(user_id=id)
