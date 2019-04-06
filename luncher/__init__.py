import configparser

from flask import Flask


app = Flask(__name__)

app_config = configparser.ConfigParser()
app_config.read('config.cfg')

app.config['SECRET_KEY'] = '29bc8b62db262b1d'

from luncher import routes
