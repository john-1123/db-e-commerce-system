from flask import request
from flask_restful import Resource
from main.services.cart_item import CartItemService

### Response for the relation of cart and product

service = CartItemService()

class GetAllCart(Resource):
    def get(self):
        return service.get_all()
    
class GetAllCartByMember(Resource):
    def get(self, id):
        return service.get_all_by_member(member_id=id)

class GetCartItem(Resource):
    def get(self):
        return service.get(data=request.json)

class AddCartItem(Resource):
    def post(self):
        return service.create(data=request.json)  

class DeleteCartItem(Resource):
    def delete(self):
        return service.delete_single(data=request.json)  

class DeleteAllCartItem(Resource): #by market and member
    def delete(self):
        return service.delete_all(data=request.json)  

class DeleteAllCartItemByMember(Resource):
    def delete(self):
        return service.delete_all_by_member(data=request.json)  

class DeleteAllCartItemByMarket(Resource):
    def delete(self):
        return service.delete_all_by_market(data=request.json)  

class ReviseCartItem(Resource):
    def put(self):
        return service.update(data=request.json)
    
