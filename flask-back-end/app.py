from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_cors import CORS
from main.controllers.auth import AuthLogin, AuthSignUp
from main.controllers.welcome import HelloWorld
from main.controllers.user import GetAllUser, GetUser, UpdateUser, DeleteUser
from main.controllers.product import GetAllProduct, GetProduct, CreateProduct, GetProductByMarket, UpdateProduct, DeleteProduct
from main.controllers.market import GetAllMarket, GetMarket, CreateMarket, GetMarketByUser, UpdateMarket, DeleteMarket
from main.models._db import db
from main.schemas._ma import ma


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/ecommerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api = Api(app, prefix='/api')
db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)

# api
api.add_resource(HelloWorld, '/')
# user api
api.add_resource(GetAllUser, '/users')
api.add_resource(GetUser, '/users/<int:id>')
api.add_resource(UpdateUser, '/users/<int:id>')
api.add_resource(DeleteUser, '/users/<int:id>')
# auth api
api.add_resource(AuthLogin, '/login')
api.add_resource(AuthSignUp, '/signup')

# product api
api.add_resource(GetAllProduct, '/products')
api.add_resource(GetProduct, '/products/<int:id>')
api.add_resource(GetProductByMarket, "/products/market/<int:id>")
api.add_resource(CreateProduct, '/products')
api.add_resource(UpdateProduct, '/products/<int:id>')
api.add_resource(DeleteProduct, '/products/<int:id>')

# market api
api.add_resource(GetAllMarket, '/markets')
api.add_resource(GetMarket, '/markets/<int:id>')
api.add_resource(GetMarketByUser, '/markets/user/<int:id>')
api.add_resource(CreateMarket, '/markets')
api.add_resource(UpdateMarket, '/markets/<int:id>')
api.add_resource(DeleteMarket, '/markets/<int:id>')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
