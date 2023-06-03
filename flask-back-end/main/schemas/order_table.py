from main.models.order_table import Order_Table
from ._ma import ma

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order_Table

