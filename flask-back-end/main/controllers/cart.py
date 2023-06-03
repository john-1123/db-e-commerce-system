from flask import request
from flask_restful import Resource
from main.services.cart import CartService

### Response for the relation of cart and order

service = CartService()

class CreateCart(Resource):
    def post(self):
        return service.create(data=request.json) 
    
### remember to reduce the product number
### or delete the quntity attribution

class GetCart(Resource):
    def get(self):
        return service.get(data=request.json)

class GetAllOrderByMarket(Resource):
    def get(self):
        return service.get_all_order_by_market(data=request.json) ### 改request.

class GetAllOrderByMember(Resource):
    def get(self):
        return service.get_all_order_by_member(data=request.json)

class DeleteCart(Resource):
    def delete(self):
        return service.delete(data=request.json)
