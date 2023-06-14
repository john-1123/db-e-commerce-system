from main.models.cart import Cart
from ._ma import ma


class CartSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cart
        include_fk = True