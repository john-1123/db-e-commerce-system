from ._db import db

class Cart(db.Model):
    __tablename__ = 'cart'
    pass

    def __init__(self):
       pass

    def arrange_data():
        data = []
        for i in range(1, 6):
            member_id = 'A%d' % i
            market_id = 'M0%d' % i
            product_id = 'P0%d' % i
            quantity = '%d00' % (i * 100)

            item = {
                "member_id":member_id,
                "market_id": market_id,
                "product_id": product_id,
                "quantity": quantity
            }

            data.append(item)

        return data

    