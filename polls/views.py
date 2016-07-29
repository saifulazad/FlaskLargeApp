__author__ = 'Azad'
from polls import feed
from flask import render_template

def feeds():
    #pass
    return render_template('home.html', a=['aaaaaa', 'sadsf', '324234'])

feed.add_url_rule('/a', 'chat', feeds)