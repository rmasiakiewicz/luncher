import configparser

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app_config = configparser.ConfigParser()
app_config.read('config.cfg')

app.config['SECRET_KEY'] = app_config['LUNCHER']['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = app_config['POSTGRES']['ADDRESS']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from luncher.users.views import users
from luncher.admin.views import admin
from luncher.main.views import main

app.register_blueprint(users)
app.register_blueprint(admin)
app.register_blueprint(main)
