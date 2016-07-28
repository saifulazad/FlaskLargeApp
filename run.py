__author__ = 'Azad'
from flask import Flask
from polls import feed
from posts import chat
from home import Home

app = Flask(__name__)
app.register_blueprint(feed)

app.register_blueprint(chat)

#app.register_blueprint(Home)

app.run(debug=True)