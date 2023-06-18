from main.models._db import save, delete
from flask import jsonify
from main.models.cart_item import CartItem
from main.models.order_table import Order_Table
from main.models.product import Product
from main.models.market import Market
from main.models.user import User
from main.schemas.user import UserSchema
import datetime

class UserService:
    def __init__(self):
        self.user_schema = UserSchema()
        self.users_schema = UserSchema(many=True)

    def get_all(self):
        users = User.query.all()
        return jsonify(self.users_schema.dump(users))

    def get(self, user_id):
        user = User.query.get(user_id)
        return self.user_schema.jsonify(user)

    def create(self, data):
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            new_user = User(
                email = data['email'],
                password = data['password'],
                username = data['username'],
                address = data['address'],
                phone = data['phone'],
                registered_on = datetime.datetime.now()
            )
            save(new_user)
            return self.user_schema.jsonify(new_user)

    def update(self, user_id, data):
        user = User.query.get(user_id)
        if user:
            user.email = data['email'],
            user.password = data['password'],
            user.username = data['username'],
            user.address = data['address'],
            user.phone = data['phone'],
            save(user)
            return self.user_schema.jsonify(user)

    def delete(self, user_id):
        user = User.query.get(user_id)
        if user:
            cart_list = CartItem.query.filter_by(member_id = user_id).all()
            for cart in cart_list:
                delete(cart)

            order_list = Order_Table.query.filter_by(member_id = user_id).all()
            for order in order_list:
                delete(order)

            market = Market.query.filter_by(user_id = user_id).first()
            if market:
                product_list = Product.query.filter_by(market_id = market.market_id).all()
                for product in product_list:
                    cart_list = CartItem.query.filter_by(product_id = product.product_id).all()
                    for cart in cart_list:
                        delete(cart)
                    delete(product)
                order_list = Order_Table.query.filter_by(market_id = market.market_id).all()
                for order in order_list:
                    delete(order)
                delete(market)
            delete(user)
            return user_id
            
