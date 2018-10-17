'''
Template: Generally speaking, it's a .html file which includes
          {{variable}}  variable could be: list dict object
                        and can use filter to transform variable, e.g {{ variable | filter }}
          and controller {% %}:
          {%if %}--{% endif %}; {%for in in list%}--{% endfor %}; {% for key, value in dict.iteritems()%}--{% endfor %}
          # and template must saved in 'templates.dir'

Jinjia2: like the frameworks of Web， there are many frameworks of templete,
         and different template has different controller
         1. controller
         # if-elif-else
         {% if condition1%}
            pass
         {% elif condition2 %}
            pass
         {% else %}
            pass
         {% endif %}

         # for in list
         {% for i in list %}
            pass
         {% endfor %}

         # for key, value in dict
         {% for key, value in dict.iteritems() %}
            pass
         {% endfor %}


         2. macro (function)
         {% macro render_comment(comment) %}
                 pass
         {% endmacro%}

         3. modules: save macro into a modules, and input it when you need
         {% import 'macro.html' as macro %}
         {{macro.render_comment(comment)}}

         4. inheritance
         <html>
         <head>
            {% block head %}
            <title>{% block title %}{% endblock %}</title>
            {% end block %}
         </head>
         <body>
             {% block body %}
             {% endblock %}
         </body>
         </html>
         where the 'block' element can be revised in its child template

         {% extends 'base.html' %}
         {% block title %}my Jinjia2 template {% endblock %}
         {% block head %}
           {{ super() }}
         {% endblock %}
         {% block body %}
         <h1>Hello, world</h1>
         {% endblock %}


render:  according to template and variable, create .html file
         render_template('view.html', variable = value)

Bootstrap: a Client framework used to design Web page
           1. from flask_bootstrap import Bootstrap  # Flask extension
           2. bootstrap = Bootstrap(app)

generate url in template:  url_for()
                           e.g.  {{url_for('home', _external=True)}}  # 'http://localhost:5000/'
                            or   {{url_for('home')}}  # '/'

Static file: image, javascript, css--> saved in static.dir
             1. generate file url:
                {{url_for('static', filename='name.type')}}
             2. load resources according to url
'''
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

# Bootstrap
@app.route('/user/<name>',methods=['GET', 'POST'])
def user(name):
    return render_template('user.html', name = name)

# error
'''
error 404:   errorhandler(exception code)
'''
@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html'), 404

# login and check out
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET', ])
def form():
    return render_template('form.html')

@app.route('/signin', methods=['POST', ])
def sinin():
    username = request.form['username']
    password = request.form['password']

    if username == 'xzq' and password == 'Cindy':
        return render_template('signin_ok.html', username = username)
    return render_template('form.html', message = 'Bad username or password', username = username)


if __name__ == "__main__":
    app.run()