from ._db import db
from main.models.market import Market

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(100))
    phone = db.Column(db.String(10))
    registered_on = db.Column(db.DateTime, nullable=False)

    market = db.relationship('Market', backref='user', uselist=False)

    def __init__(self, email, password, username, address, phone, registered_on):
        self.email = email
        self.password = password
        self.username = username
        self.address = address
        self.phone = phone
        self.registered_on = registered_on