from .resources.status import Status
from app.api.resources.product import Product, Products


def init_routes(api):
    """routes"""
    api.add_resource(Status, '/status')
    api.add_resource(Products, '/products')
    api.add_resource(Product, '/product/<int:_id>')