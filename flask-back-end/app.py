from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_cors import CORS
from main.controllers.auth import AuthLogin, AuthSignUp
from main.controllers.welcome import HelloWorld
from main.controllers.user import GetAllUser, GetUser, UpdateUser, DeleteUser,CreateUser
from main.controllers.cart_item import GetCartItem,AddCartItem,DeleteCartItem,ReviseCartItem,GetAllCart,DeleteAllCartItem,DeleteAllCartItemByMarket,DeleteAllCartItemByMember
from main.controllers.cart import GetCart,GetAllOrderByMember,GetAllOrderByMarket,CreateCart,DeleteCart
from main.controllers.order_table import GetOrder,UpdateOrder
# from main.controllers.order_table import GetOrder,CreateOrder,UpdateOrder,DeleteOrder
from main.models._db import db
from main.schemas._ma import ma

passwd=""
with open(r"C:\Users\User\Desktop\passwd.txt",mode="r") as file:
    for i in file:
        passwd=i

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:'+passwd+'@localhost:3306/ecommerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api = Api(app, prefix='/api')
db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)

# api
api.add_resource(HelloWorld, '/')

# user api
#in json <email ,password ,username,address ,phone >

api.add_resource(GetAllUser, '/users')
api.add_resource(GetUser, '/users/<int:id>')
api.add_resource(UpdateUser, '/users/<int:id>')
api.add_resource(DeleteUser, '/users/<int:id>')
api.add_resource(CreateUser,'/users')

# auth api
api.add_resource(AuthLogin, '/login')
api.add_resource(AuthSignUp, '/signup')

#cart_item api
#in json <member_id=,market_id=,product_id=,quntity=>
#in method <get,post,delete,put>
api.add_resource(GetCartItem,'/cart_item')
api.add_resource(AddCartItem,'/cart_item')
api.add_resource(DeleteCartItem,'/cart_item')
api.add_resource(ReviseCartItem,'/cart_item')
api.add_resource(GetAllCart,'/cart_item_all')
api.add_resource(DeleteAllCartItem,'/cart_item_all')
api.add_resource(DeleteAllCartItemByMember,'/cart_item_all_by_member')
api.add_resource(DeleteAllCartItemByMarket,'/cart_item_all_by_market')

#cart api
#in json <member_id=,market_id=,order_id=>
#in method <get,post,delete>
api.add_resource(GetCart,'/cart')
api.add_resource(CreateCart,'/cart')
api.add_resource(DeleteCart,'/cart')
api.add_resource(GetAllOrderByMarket,'/cart_all_by_market')
api.add_resource(GetAllOrderByMember,'/cart_all_by_member')

#order api
#in json <order_id=,state=,shipping_address,payment_method,mode_of_transport>
#in method <get,post,delete>
api.add_resource(GetOrder,'/order')
# api.add_resource(CreateOrder,'/order')
# api.add_resource(DeleteOrder,'/order')
api.add_resource(UpdateOrder,'/order')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
