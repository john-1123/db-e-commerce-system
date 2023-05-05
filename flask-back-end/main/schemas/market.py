from main.models.market import Market
from ._ma import ma

class MarketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Market

