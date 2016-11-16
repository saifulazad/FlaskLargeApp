__author__ = 'Azad'

from flask import Blueprint

import sys



feed = Blueprint('feed', __name__)


def reverse_filter(s):
    return s[::-1]
from polls import views