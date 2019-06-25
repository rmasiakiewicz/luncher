# coding=utf-8
from luncher import db


class Dish(db.Model):

    __tablename__ = 'dish'

    dish_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id'))
    dish_type = db.Column(db.Integer)
    price = db.Column(db.Numeric)
    __table_args__ = (db.UniqueConstraint('name', 'supplier_id'),)

    def __repr__(self):
        return f"Dish('{self.name}', from supplier: '{self.supplier_id}')"
