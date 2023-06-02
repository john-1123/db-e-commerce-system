from ._db import db
from .user import User
from .market import Market
from .order_table import Order_Table

class Cart(db.Model):
    __tablename__ = 'cart'
    member_id = db.Column(db.Integer, db.ForeignKey('user.user_id'),primary_key=True,nullable=False)
    market_id = db.Column(db.Integer, db.ForeignKey('market.market_id'),primary_key=True,nullable=False)

    # order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'),primary_key=True,nullable=False)
    order_id = db.Column(db.Integer,primary_key=True,nullable=False)


    def __init__(self,member_id,market_id,order_id):
        self.member_id=member_id
        self.market_id=market_id
        self.order_id=order_id
        