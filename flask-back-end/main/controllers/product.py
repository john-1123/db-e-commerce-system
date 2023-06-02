from flask import request
from flask_restful import Resource
from main.services.product import ProductService

service = ProductService()

class GetAllProduct(Resource):
    def get(self):
        return service.get_all()

class GetProduct(Resource):
    def get(self, id):
        return service.get(product_id=id)

class CreateProduct(Resource):
    def post(self):
        return service.create(data=request.json)

class UpdateProduct(Resource):
    def put(self, id):
        return service.update(product_id=id, data=request.json)

class DeleteProduct(Resource):
    def delete(self, id):
        return service.delete(product_id=id)
    
class GetProductByMarket(Resource):
    def get(self, id):
        products = service.get_all_by_market(market_id=id)
        print(products)
        return products