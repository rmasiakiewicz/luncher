# coding=utf-8
from luncher import db


class Basket(db.Model):

    __tablename__ = 'basket'

    basket_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    info = db.Column(db.JSON, nullable=False)

    order = db.relationship("Order", uselist=False, backref="basket")

    def __repr__(self):
        return f"Basket('{self.basket_id}')"
