# coding=utf-8

from database.base import Base, engine
from database.dish import Dish
from database.basket import Basket
from database.order import Order
from database.supplier import Supplier
from database.user import User

Base.metadata.create_all(bind=engine, checkfirst=True)
