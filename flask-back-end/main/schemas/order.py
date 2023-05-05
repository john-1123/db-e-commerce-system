from main.models.order import Order
from ._ma import ma

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order

