from app.api.models.variant import VariantModel
from app.ma import ma


class VariantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VariantModel
        load_instance = True
        dump_only = ("id",)
        ordered = True
        include_fk = True
