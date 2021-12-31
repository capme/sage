from app.api.models.product import ProductModel
from app.ma import ma


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        load_instance = True
        dump_only = ("id",)
        ordered = True
        include_fk = True
