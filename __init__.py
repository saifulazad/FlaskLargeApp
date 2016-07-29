from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

__author__ = 'Azad'
app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)
