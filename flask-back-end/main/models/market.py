from ._db import db

class Market(db.Model):
    __tablename__ = 'market'
    market_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __init__(self):
        pass