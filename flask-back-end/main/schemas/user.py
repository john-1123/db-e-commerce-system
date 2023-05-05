from main.models.user import User
from ._ma import ma

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

