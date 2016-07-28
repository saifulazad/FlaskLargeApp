__author__ = 'Azad'
from . import chat

@chat.route('/chat')
def chat():
    return 'chat'