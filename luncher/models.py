# coding=utf-8
import datetime

from luncher import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    level = db.Column(db.Integer, default=1)
    orders = db.relationship("Order", backref="users")

    def __repr__(self):
        return f"User('{self.name}', '{self.surname}', '{self.email}')"


class Order(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    basket_id = db.Column(db.Integer, db.ForeignKey('basket.id'), unique=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    __table_args__ = (db.UniqueConstraint('user_id', 'date'),)

    def __repr__(self):
        return f"Order(from users: '{self.user_id}', date: '{self.date}')"


class Basket(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    info = db.Column(db.JSON, nullable=False)

    order = db.relationship("Order", uselist=False, backref="basket")

    def __repr__(self):
        return f"Basket('{self.id}')"


class Dish(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    dish_type = db.Column(db.Integer)
    price = db.Column(db.Numeric)
    __table_args__ = (db.UniqueConstraint('name', 'supplier_id'),)

    def __repr__(self):
        return f"Dish('{self.name}', from supplier: '{self.supplier_id}')"


class Supplier(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)

    dishes = db.relationship("Dish", backref="supplier")

    def __repr__(self):
        return f"Supplier('{self.name}')"
