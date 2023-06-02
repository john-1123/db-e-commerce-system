from ._db import db
from .market import Market
from .user import User
from .product import Product

class CartItem(db.Model):
    __tablename__ = 'cart_item'
    member_id = db.Column(db.Integer, db.ForeignKey('user.user_id'),primary_key=True,nullable=False)
    market_id = db.Column(db.Integer, db.ForeignKey('market.market_id'),primary_key=True,nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'),primary_key=True,nullable=False)
    quntity = db.Column(db.Integer, nullable=False)

    def __init__(self,member_id,market_id,product_id,quntity):
        self.member_id=member_id
        self.market_id=market_id
        self.product_id=product_id
        self.quntity=quntity
        