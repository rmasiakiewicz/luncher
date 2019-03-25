# coding=utf-8
from sqlalchemy import Column, Integer, UniqueConstraint, DATE, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class Order(Base):

    __tablename__ = 'order'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    basket_id = Column(Integer)
    date = Column(DATE)
    __table_args__ = (UniqueConstraint('user_id', 'date'),)

    basket = relationship("Basket", back_populates="order")
    user = relationship("User", back_populates="orders")

    def __init__(self, user_id, basket_id, date):
        self.user_id = user_id
        self.basket_id = basket_id
        self.date = date
