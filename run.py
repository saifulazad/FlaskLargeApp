import jinja2

__author__ = 'Azad'
from flask import Flask
from polls import feed
from posts import chat
from home import Home
#
# loader=jinja2.FileSystemLoader('templates')
app = Flask(__name__)


@app.template_filter('upper')
def reverse_filter(s):
    return ['TK :'+x.upper() for x in s]

app.register_blueprint(feed)

app.register_blueprint(chat)

app.register_blueprint(Home)
#app.register_blueprint(Home)

app.run(debug=True)