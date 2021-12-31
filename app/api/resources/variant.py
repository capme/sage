from flask import request
from flask_restful import Resource
from app.api.models.variant import VariantModel
from app.api.schemas.variant import VariantSchema
import datetime


variants_schema = VariantSchema(many=True)
variant_schema = VariantSchema()


class Variants(Resource):
    def get(self):
        return variants_schema.dump(VariantModel.find_all()), 200


class Variant(Resource):
    def get(cls, _id):
        variant = VariantModel.find_by_id(_id)
        if variant:
            return variant_schema.dump(variant), 200

        return {'msg': 'Sorry no value found'}, 404

    @classmethod
    def post(cls):
        variant = variant_schema.load(request.get_json())
        if variant.find_by_uri(variant.uri_check):
            return {'msg': 'The data you are trying to add is already added.'}, 401

        variant.add_to_db()
        return {'msg': 'The variant has been created', 'variant_id': variant.id}, 201

    @classmethod
    def put(cls, _id: int):
        variant_json = request.get_json()
        variant = VariantModel.find_by_id(_id)

        if variant:
            variant.name = variant_json['name']
            variant.product_id = variant_json.get('product_id')
            variant.size = variant_json['size']
            variant.color = variant_json['color']
            variant.images = variant_json['images']  # url1, url2, url3, ...., etc
            variant.updated_at = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '%Y-%m-%d %H:%M:%S')

            variant.add_to_db()
            return variant_schema.dump(variant), 200
        return {'msg': 'The variant does not exist'}, 404
