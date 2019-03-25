# coding=utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.base import Base


class User(Base):

    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    level = Column(Integer)

    orders = relationship("Order", back_populates="user")

    def __init__(self, user_id, name, surname, email, password, level):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.level = level
