__author__ = 'Azad'
from home import Home

@Home.route('/home')
def home():
    return 'Home'