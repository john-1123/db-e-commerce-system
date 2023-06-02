from main.models._db import save, delete
from flask import jsonify
from main.models.product import Product
from main.schemas.product import ProductSchema
# import datetime

class ProductService:
    def __init__(self):
        self.product_schema = ProductSchema()
        self.products_schema = ProductSchema(many=True)

    def get_all(self):
        products = Product.query.all()
        return jsonify(self.products_schema.dump(products))

    def get(self, product_id):
        product = Product.query.get(product_id)
        return self.product_schema.jsonify(product)

    def create(self, data):
        product = Product.query.filter_by(product_name = data['product_name']).first()
        if not product:
            new_product = Product(
                product_name= data['product_name'],
                category= data['category'],
                brand = data['brand'],
                price = data['price'],
                stock = data['stock'],
                market_id =  data['market_id'],
                status = data['status'],
            )

            save(new_product)
            return self.product_schema.jsonify(new_product)

    def update(self, product_id, data):
        product = Product.query.get(product_id)
        if product:
            product.product_name = data['product_name'],
            product.category = data['category'],
            product.brand = data['brand'],
            product.price = data['price'],
            product.stock = data['stock'],
            product.market_id = data['market_id'],
            product.status = data['status']
            save(product)
            return self.product_schema.jsonify(product)

    def delete(self, product_id):
        product = Product.query.get(product_id)
        if product:
            delete(product)
            return product_id