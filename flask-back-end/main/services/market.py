from main.models._db import save, delete
from flask import jsonify
from main.models.user import User
from main.models.market import Market
from main.schemas.market import MarketSchema
import datetime

class MarketService:
    def __init__(self):
        self.market_schema = MarketSchema()

    def get_all(self):
        markets = Market.query.all()
        return jsonify(self.market_schema.dump(markets))

    def get(self, market_id):
        market = Market.query.get(market_id)
        return self.market_schema.jsonify(market)

    def create(self, market_id, data=None):
        market = Market.query.get(market_id)
        if not market:
            user_id = data.get('user_id')  
            user = User.query.get(user_id)
            if not user:
                return "User not found", 404
            
            new_market = Market(
                market_name = data['market_name'],
                uid = user.user_id,
                registered_on = datetime.datetime.now()
            )
            save(new_market)
            return self.market_schema.jsonify(new_market)

    def update(self, market_id, data):
        market = Market.query.get(market_id)
        if market:
            market.market_name = data['market_name'],
            save(market)
            return self.market_schema.jsonify(market)

    def delete(self, market_id):
        market = Market.query.get(market_id)
        if market:
            delete(market)
            return market_id
