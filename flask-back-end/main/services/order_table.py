from main.models._db import save, delete
from flask import jsonify
from main.models.order_table import Order_Table
from main.schemas.order_table import OrderSchema
import datetime

class OrderService:
    def __init__(self):
        self.order_schema = OrderSchema()
        self.orders_schema = OrderSchema(many=True)

    def get(self, data):
        order = Order_Table.query.get(data['order_id'])
        return self.order_schema.jsonify(order)

    # def create(self, data):
    #     # order = Order.query.filter_by(order_id=data['order_id']).first()
    #     # if not order:
    #     new_order = Order_Table(
    #         state=data['state'],
    #         shipping_address=data['shipping_address'],                
    #         consignee=data['consignee'],
    #         payment_method=data['payment_method'],
    #         mode_of_transport=data['mode_of_transport'],
    #         member_id=data['member_id'],
    #     )
    #     save(new_order)
    #     return self.order_schema.jsonify(new_order)

    def update(self, data):
        order = Order_Table.query.get(data['order_id'])
        if order:
            order.state=data['state'],
            order.shipping_address=data['shipping_address'],
            order.consignee=data['consignee'],
            order.payment_method=data['payment_method'],
            order.mode_of_transport=data['mode_of_transport'],
            order.member_id=data['member_id'],
            order.last_modified_time=datetime.datetime.now()
            save(order)
            return self.order_schema.jsonify(order)

    # def delete(self,data):
    #     order = Order_Table.query.get(data['order_id'])
    #     if order:
    #         delete(order)
    #         return data['order_id']
