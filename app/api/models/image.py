from app.db import db
from typing import List


class ImageModel(db.Model):
    """
    Images model
    """
    __tablename__ = "image"
    __table_args__ = ({'mysql_engine':'InnoDB', 'mysql_charset':'utf8mb4','mysql_collate':'utf8mb4_0900_ai_ci'}, )

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text(100000), nullable=False)

    def __repr__(self):
        return "<ImageModel {}>".format(self.url)

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id: int) -> "ImageModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["ImageModel"]:
        return cls.query.all()
