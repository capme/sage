from .resources.status import Status
from app.api.resources.product import Product, Products
from app.api.resources.variant import Variant, Variants


def init_routes(api):
    """routes"""
    api.add_resource(Status, '/status')
    api.add_resource(Products, '/products')
    api.add_resource(Product, '/product/', '/product/<int:_id>')
    api.add_resource(Variants, '/variants')
    api.add_resource(Variant, '/variant/', '/variant/<int:_id>')