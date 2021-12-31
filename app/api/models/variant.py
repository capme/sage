from app.db import db
from typing import List


class VariantModel(db.Model):
    """
    Products model
    """
    __tablename__ = "variant"
    __table_args__ = ({'mysql_engine':'InnoDB', 'mysql_charset':'utf8mb4','mysql_collate':'utf8mb4_0900_ai_ci'}, )

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete='SET NULL'))
    name = db.Column(db.String(80), nullable=False)
    size = db.Column(db.String(80))  # not always integer for the size
    color = db.Column(db.String(80))
    images = db.Column(db.Text(100000))  # only PostgreSQL support for data type db.ARRAY in SQL Alchemy
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return "<VariantModel {}>".format(self.name)

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name: str) -> "VariantModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "VariantModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["VariantModel"]:
        return cls.query.all()
