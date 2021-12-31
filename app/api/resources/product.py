from flask import request
from flask_restful import Resource
from app.api.models.product import ProductModel
from app.api.schemas.product import ProductSchema
import datetime


products_schema = ProductSchema(many=True)
product_schema = ProductSchema()


class Products(Resource):
    def get(self):
        return products_schema.dump(ProductModel.find_all()), 200


class Product(Resource):
    def get(cls, _id):
        product = ProductModel.find_by_id(_id)
        if product:
            return product_schema.dump(product), 200

        return {'msg': 'Sorry no value found'}, 404

    @classmethod
    def post(cls):
        product = product_schema.load(request.get_json())
        if product.find_by_uri(product.uri_check):
            return {'msg': 'The data you are trying to add is already added.'}, 401

        product.add_to_db()
        return {'msg': 'The product has been created', 'product_id': product.id}, 201

    @classmethod
    def put(cls, _id: int):
        product_json = request.get_json()
        product = ProductModel.find_by_id(_id)

        if product:
            product.name = product_json['name']
            product.description = product_json['description']
            product.logo_id = product_json.get('logo_id')
            product.updated_at = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '%Y-%m-%d %H:%M:%S')

            product.add_to_db()
            return product_schema.dump(product), 200
        return {'msg': 'The product does not exist'}, 404
