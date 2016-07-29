from flask import render_template
from . import chat

#
# @chat.route('/chat')
# def chat():
#     return 'chat'
#
from flask.views import View, MethodView


class ListView(View):

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        return self.render_template(context)

class UserView(ListView):

    def get_template_name(self):
        return 'chat_list.html'

    def get_objects(self):
        return ['Azad', 'Jamil', 'Saarah']


class ShowUsers(View):

    def dispatch_request(self):
        users = ['Azad', 'Sadi', 'Saarah']
        return render_template('chat.html', chat='AAAvAA')
#
# class ChatDetails(MethodView):
#     pass
#
# class ArticleView(DetailView):
#     get_fields = {
#         'category': 'category',
#         'slug': 'slug',
#     }
#     # For creating document classes, see the Mongoengine documentation
#     document_class = Article
#     template_name = 'article_detail.html'
#
# app.add_url_rule(
#     '/articles/<category>/<slug>/',
#     view_func=ArticleView.as_view('article')
# )
@chat.route('/chat/<page>')
def show(page):
    return render_template('chat_details.html' , x = page)






chat.add_url_rule('/chat/', view_func=ShowUsers.as_view('show_users'))

chat.add_url_rule('/chat_list/', view_func=UserView.as_view('show_users_list'))

# chat.add_url_rule('/chat', 'chat', chat)