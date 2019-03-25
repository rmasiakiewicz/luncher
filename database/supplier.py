# coding=utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.base import Base


class Supplier(Base):

    __tablename__ = 'supplier'

    supplier_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)

    dishes = relationship("Dish", back_populates="supplier")

    def __init__(self, name):
        self.name = name
