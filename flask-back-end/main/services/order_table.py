from main.models._db import save, delete
from flask import jsonify
from main.models.order_table import Order_Table
from main.schemas.order_table import OrderSchema
from main.models.product import Product
from main.models.cart_item import CartItem

import datetime

class OrderService:
    def __init__(self):
        self.order_schema = OrderSchema()
        self.orders_schema = OrderSchema(many=True)

    def get(self, data):
        order = Order_Table.query.filter(Order_Table.order_id==data['order_id']).first()
      
        if order== None:
            return "not found"
        else: 
            return self.order_schema.jsonify(order)
    
    def get_all_order_by_market(self, market_id):
        order_list = Order_Table.query.filter_by(market_id=market_id).all()
        return self.orders_schema.jsonify(order_list)

    def get_all_order_by_member(self, user_id):
        order_list = Order_Table.query.filter_by(member_id=user_id).all()
        return self.orders_schema.jsonify(order_list)

    def create(self, data):

        ### pull from cart
        items = CartItem.query.filter(CartItem.member_id==data['member_id'],CartItem.market_id==data['market_id']).all()

        cost=0
        items_list=[]
        quntity_list=[]
        cash_list=[]
        
        if len(items)==0:
            return "Can't make order"
        
  
        for item in items:
            product_id=item.product_id
            demand=item.quntity
            
            this_product = Product.query.filter(Product.product_id==product_id).first()
            price=this_product.price
            supply=this_product.stock
            item_name=this_product.product_name
            
            items_list.append(item_name)
            quntity_list.append(str(demand))
            cash_list.append(str(price*demand))
            
            if supply<demand:
                return "You Buy Too Much"
            else:
                cost+=price*demand
            
            
        ### check 

        new_order = Order_Table(
            member_id=data['member_id'],
            market_id=data['market_id'],
            state=data['state'],
            shipping_address=data['shipping_address'],                
            consignee=data['consignee'],
            payment_method=data['payment_method'],
            mode_of_transport=data['mode_of_transport'],
            items = ",".join(items_list),
            quntities = ",".join(quntity_list),
            cashs = ",".join(cash_list),
            cost = cost
        )
        
        save(new_order)
           
        order_id=new_order.order_id
        print("new order_id=",order_id)

        return self.order_schema.jsonify(new_order)

    # def update(self, data):
    #     order = Order_Table.query.get(data['order_id'])
    #     if order:
    #         order.state=data['state'],
    #         order.shipping_address=data['shipping_address'],
    #         order.consignee=data['consignee'],
    #         order.payment_method=data['payment_method'],
    #         order.mode_of_transport=data['mode_of_transport'],
    #         order.member_id=data['member_id'],
    #         order.last_modified_time=datetime.datetime.now()
    #         save(order)
    #         return self.order_schema.jsonify(order)

    def delete(self, order_id):
        order = Order_Table.query.filter_by(order_id=order_id).first()
        if order:
            delete(order)
            return self.order_schema.jsonify(order)
