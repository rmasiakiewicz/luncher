# coding=utf-8
import datetime

from luncher import db


class Order(db.Model):

    __tablename__ = 'order'

    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    basket_id = db.Column(db.Integer, db.ForeignKey('basket.basket_id'), unique=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    __table_args__ = (db.UniqueConstraint('user_id', 'date'),)

    def __repr__(self):
        return f"Order(from user: '{self.user_id}', date: '{self.date}')"

