from ._db import db
# from main.models.cart import Cart

class Market(db.Model):
    __tablename__ = 'market'
    market_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    market_name = db.Column(db.String(20), unique=True, nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    # pid = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    registered_on = db.Column(db.DateTime, nullable=False)

    # cart = db.relationship('Cart', backref='market')

    def __init__(self, market_id, market_name, registered_on):
        self.market_name = market_name
        self.registered_on = registered_on