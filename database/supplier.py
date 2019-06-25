# coding=utf-8
from luncher import db


class Supplier(db.Model):

    __tablename__ = 'supplier'

    supplier_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)

    dishes = db.relationship("Dish", backref="supplier")

    def __repr__(self):
        return f"Supplier('{self.name}')"
