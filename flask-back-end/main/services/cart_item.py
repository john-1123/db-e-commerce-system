from main.models._db import delete, save
from main.models.cart_item import CartItem
from main.schemas.cart_item import CartItemSchema


class CartItemService:
    def __init__(self):
        self.cart_schema = CartItemSchema()
        self.carts_schema = CartItemSchema(many=True)

    def get_all(self):
        cart_list = CartItem.query.all()
        return self.carts_schema.jsonify(cart_list)
    
    def get_all_by_member(self, member_id):
        item_list = CartItem.query.filter_by(member_id=member_id).all()
        return self.carts_schema.jsonify(item_list)
    
    def get(self, data):
        cart = CartItem.query.filter_by(member_id = data['member_id'], market_id = data['market_id']).first()
        return self.cart_schema.jsonify(cart)

    def create(self, data):
        cart = CartItem.query.filter_by(member_id = data['member_id'], market_id = data['market_id'], product_id = data['product_id']).first()
        if not cart:
            cart = CartItem(
                member_id = data['member_id'],
                market_id = data['market_id'],
                product_id = data['product_id'],
                quantity = data['quantity']
            )
            save(cart)
            return self.cart_schema.jsonify(cart)
        else:
            cart.quantity += int(data['quantity'])
            save(cart)
            return self.cart_schema.jsonify(cart)

    def update(self,data):
        cart = CartItem.query.filter_by(member_id = data['member_id'], market_id = data['market_id'], product_id = data['product_id']).first()
        if cart:
            cart.quantity = data['quantity']
            save(cart)
            return self.cart_schema.jsonify(cart)

    def delete_single(self, user_id, market_id, product_id):
        cart = CartItem.query.filter_by(member_id=user_id, market_id=market_id, product_id=product_id).first()
        if cart:
            delete(cart)
            return self.cart_schema.jsonify(cart)
        
    def delete_all(self, data):
        cart_list = CartItem.query.filter_by(member_id = data['member_id'], market_id = data['market_id']).all()
        if len(cart_list) != 0:
            for cart in cart_list:
                delete(cart)
            return "All the record of User #" + str(data['member_id']) + " in market #" + str(data['market_id']) + " has been deleted"


    def delete_all_by_member(self, data):
        cart_list = CartItem.query.filter_by(member_id = data['member_id']).all()
        if len(cart_list) != 0:
            for cart in cart_list:
                delete(cart)
            return self.carts_schema(cart_list)

    def delete_all_by_market(self, data):
        cart_list = CartItem.query.filter_by(member_id = data['member_id'], market_id = data['market_id']).all()
        if len(cart_list)!=0:
            for cart in cart_list:
                delete(cart)
            return self.carts_schema(cart_list)
