import configparser

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app_config = configparser.ConfigParser()
app_config.read('config.cfg')

app.config['SECRET_KEY'] = '29bc8b62db262b1d'
app.config['SQLALCHEMY_DATABASE_URI'] = app_config['POSTGRES']['ADDRESS']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from luncher import routes
