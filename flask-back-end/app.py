from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_cors import CORS
from main.controllers.auth import AuthLogin, AuthSignUp
from main.controllers.welcome import HelloWorld
from main.controllers.user import GetAllUser, GetUser, UpdateUser, DeleteUser
from main.models._db import db
from main.schemas._ma import ma


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:S111753141@localhost:3306/ecommerce'
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

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
