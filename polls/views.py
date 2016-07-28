__author__ = 'Azad'
from polls import feed

@feed.route('/feed')
def feed():
    return 'feed'