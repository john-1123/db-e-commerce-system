from ._db import db
from main.models.cart_item import CartItem

class Product(db.Model):
    __tablename__ = 'product'
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(20), unique=True, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    brand = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    market_id = db.Column(db.Integer, db.ForeignKey("market.market_id"), nullable=False)
    cart_item = db.relationship('cart_item', backref='product')

    def __init__(self, product_name, category, brand, price, stock, market_id):
        self.product_name = product_name
        self.category = category
        self.brand = brand
        self.price = price
        self.stock = stock
        self.market_id = market_id