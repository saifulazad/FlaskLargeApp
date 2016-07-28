__author__ = 'Azad'
from home import Home

@Home.route('/')
def home():
    return 'Home'