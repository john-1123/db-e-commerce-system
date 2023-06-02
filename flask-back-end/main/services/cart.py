from main.models._db import save, delete
from flask import jsonify
from main.models.cart import Cart
from main.models.order_table import Order_Table
from main.schemas.cart import CartSchema

class CartService:
    def __init__(self):
        self.cart_schema = CartSchema()
        self.carts_schema = CartSchema(many=True)

    def get(self, data):
        cart = Cart.query.filter(Cart.order_id==data['order_id']).first()
        # cart = Cart.query.filter(Cart.member_id==data['member_id'],Cart.market_id==data['market_id'],Cart.order_id==data['order_id'])
        return {"member_id":cart.member_id,"market_id":cart.market_id,"order_id":cart.order_id}
    
    def get_all_order_by_market(self, data):
        cart = Cart.query.filter(Cart.market_id==data['market_id']).all()
        return self.carts_schema.jsonify(cart)

    def get_all_order_by_member(self, data):
        cart = Cart.query.filter(Cart.member_id==data['member_id']).all()
        return self.carts_schema.jsonify(cart)

    def create(self, data): ### 小心重複下訂

        check_product=True

        ### go to product and check the number

        ### count for the money

        if check_product:
            new_order = Order_Table(
                state=data['state'],
                shipping_address=data['shipping_address'],                
                consignee=data['consignee'],
                payment_method=data['payment_method'],
                mode_of_transport=data['mode_of_transport'],
                member_id=data['member_id'],
            )
            save(new_order)

           
            order_id=new_order.order_id
            print("new order_id=",order_id)

            new_cart = Cart(
                member_id=data['member_id'],
                market_id=data['market_id'],
                order_id=order_id
            )
            save(new_cart)
            return self.cart_schema.jsonify(new_cart)

    def delete(self,data):

        cart = Cart.query.filter(Cart.order_id==data['order_id']).first()
        if cart:
            delete(cart)

            order = Order_Table.query.get(data['order_id'])
            if order:
                delete(order)
                return data['order_id']
