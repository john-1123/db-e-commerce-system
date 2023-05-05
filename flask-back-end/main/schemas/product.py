from main.models.product import Product
from ._ma import ma

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

