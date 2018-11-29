'''
MVC(Model View Controller):
           @app.route('/url',methods=['GET','POST'])
           def ViewFunction:
               variable = None
               ...
               return render_template('file.html',variable = variable)  # from flask import render_template
           # where to separate 'data-controller' and 'page-presenter',
           we further divided 'ViewFunction' into: 'Controller' is the mainer of ViewFunction, and the duty is to deal with the 'Request' from client
                                                                and generate corresponding 'Model'(e.g. variable) which will be transmitted to 'Viewer'
                                                    'Viewer' is a Template (e.g. file.html), who get the 'Model' and render html file

Template(Jinja2): is a special '.html' file inserted  {{ variable}} and {% Controller %} and the .py can directly insert into the .html file
                  all templates will be saved into 'templates' (dir)
                  {{ variable | [filter] }}: where 'variable' includes: obj, list, dict
                                             filter: safe  # don't translate
                  {% Controller %}...{% endController %}:  {% if condition%}, {% for in iterable %},
                                                           {% macro function() %} # function
                                                           {% import 'macros.html' %} # modules
                  inherit: {% extend 'base.html' %}
                           {% block tag %}...{% endblock %}

Bootstrap: Flask-Bootstrap

Get dynamic url: from flask import url_for
                 url_for('ViewFunction', **kwargs, [_external=False/True])  # return the url of 'ViewFunction'

Static file: images, .js, .css
             url: /static/<filename>     {{ url_for('static',filename='filename')}}
'''
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/<name>',methods=['GET','POST'])
def Welcome(name):
    return render_template('welcome.html',name = name)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html',current_time = datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()

# # login and check out
# @app.route('/',methods=['GET','POST'])
# def home():
#     return render_template('home.html')
#
# @app.route('/signin', methods=['GET', ])
# def form():
#     return render_template('form.html')
#
# @app.route('/signin', methods=['POST', ])
# def sinin():
#     username = request.form['username']
#     password = request.form['password']
#
#     if username == 'xzq' and password == 'Cindy':
#         return render_template('signin_ok.html', username = username)
#     return render_template('form.html', message = 'Bad username or password', username = username)
