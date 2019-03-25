# coding=utf-8
import configparser

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()
config.read('config.cfg')

engine = create_engine(config['POSTGRES']['ADDRESS'])
session = sessionmaker(bind=engine)

Base = declarative_base()
