from ._db import db
from sqlalchemy import Column, Integer, ForeignKey

class CartItem(db.Model):
    __tablename__ = 'cart_item'
    member_id = Column(Integer, ForeignKey('user.user_id'), primary_key = True, nullable = False)
    market_id = Column(Integer, ForeignKey('market.market_id'), primary_key = True, nullable = False)
    product_id = Column(Integer, ForeignKey('product.product_id'), primary_key = True, nullable = False)
    quantity = Column(Integer, nullable = False)

    def __init__(self, member_id, market_id, product_id, quantity):
        self.member_id = member_id
        self.market_id = market_id
        self.product_id = product_id
        self.quantity = quantity
        