# coding=utf-8
from sqlalchemy import Column, Integer, Numeric
from sqlalchemy.orm import relationship

from database.base import Base
from database.dish import dish_basket_association_table


class Basket(Base):

    __tablename__ = 'basket'

    basket_id = Column(Integer, primary_key=True, autoincrement=True)
    soup_id = Column(Integer)
    main_dish_id = Column(Integer)
    total_price = Column(Numeric)

    order = relationship("Order", uselist=False, back_populates="basket")
    dishes = relationship("Dish", secondary=dish_basket_association_table, back_populates="baskets")

    def __init__(self, name, supplier_id, dish_type, price):
        self.name = name
        self.supplier_id = supplier_id
        self.dish_type = dish_type
        self.price = price
