# coding=utf-8
from luncher import db


class User(db.Model):

    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Strin)
    surname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    level = db.Column(db.Integer, default=1)

    orders = db.relationship("Order", backref="user")

    def __repr__(self):
        return f"User('{self.name}', '{self.surname}', '{self.email}')"
