from ._db import db
from .user import User
import datetime


class Order_Table(db.Model):
    __tablename__ = 'order_table'

    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False) 
    last_modified_time = db.Column(db.DateTime, nullable=False) 
    shipping_address = db.Column(db.String(100), nullable=False)
    consignee = db.Column(db.String(20), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    mode_of_transport = db.Column(db.String(50)) 
    member_id = db.Column(db.Integer, db.ForeignKey('user.user_id'),nullable=False)

    def __init__(self,state,shipping_address,consignee,payment_method,mode_of_transport,member_id):
        self.state=state
        self.create_time=datetime.datetime.now()
        self.last_modified_time=datetime.datetime.now()
        self.shipping_address=shipping_address
        self.consignee=consignee
        self.payment_method=payment_method
        self.mode_of_transport=mode_of_transport
        self.member_id=member_id