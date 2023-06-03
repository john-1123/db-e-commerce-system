from main.models.cart_item import CartItem
from ._ma import ma

class CartItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CartItem

