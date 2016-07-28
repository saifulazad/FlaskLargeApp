__author__ = 'Azad'
from flask import Blueprint

Home = Blueprint('home', __name__, url_prefix='/home')

import views