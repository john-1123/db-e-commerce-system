from ._db import db
from main.models.product import Product
# from main.models.cart import Cart
# from main.models.cart_item import CartItem

class Market(db.Model):
    __tablename__ = 'market'
    market_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    market_name = db.Column(db.String(20), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)

    # cart = db.relationship('cart', backref='market')
    # cart_item = db.relationship('cart_item', backref='market')
    product = db.relationship('Product', backref='market')

    def __init__(self, market_name, user_id, registered_on):
        self.market_name = market_name
        self.user_id = user_id
        self.registered_on = registered_on