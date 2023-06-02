from flask import request
from flask_restful import Resource
from main.services.market import MarketService

service = MarketService()

class GetAllMarket(Resource):
    def get(self):
        return service.get_all()

class GetMarket(Resource):
    def get(self, id):
        return service.get(market_id=id)

class CreateMarket(Resource):
    def post(self):
        return service.create(data=request.json)

class UpdateMarket(Resource):
    def put(self, id):
        return service.update(market_id=id, data=request.json)

class DeleteMarket(Resource):
    def delete(self, id):
        return service.delete(market_id=id)