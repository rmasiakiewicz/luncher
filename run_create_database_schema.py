# coding=utf-8

from luncher import db
db.session.close_all()
db.drop_all()
db.create_all()
