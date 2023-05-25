from ._db import db

class Product(db.Model):
    __tablename__ = 'product'
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __init__(self):
        pass