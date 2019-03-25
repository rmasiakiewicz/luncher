# coding=utf-8
from sqlalchemy import Column, Integer, String, Numeric, UniqueConstraint, ForeignKey, Table
from sqlalchemy.orm import relationship

from database.base import Base

dish_basket_association_table = Table('dishes_baskets_association', Base.metadata,
                                      Column('dish_id', Integer, ForeignKey('dish.dish_id')),
                                      Column('basket_id', Integer, ForeignKey('basket.basket_id')))


class Dish(Base):

    __tablename__ = 'dish'

    dish_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    supplier_id = Column(Integer, ForeignKey('supplier.supplier_id'))
    dish_type = Column(Integer)
    price = Column(Numeric)
    __table_args__ = (UniqueConstraint('name', 'supplier_id'),)

    supplier = relationship("Supplier", back_populates="dishes")
    baskets = relationship("Basket", secondary=dish_basket_association_table, back_populates='dishes')

    def __init__(self, name, supplier_id, dish_type, price):
        self.name = name
        self.supplier_id = supplier_id
        self.dish_type = dish_type
        self.price = price
