'''
Template: Generally speaking, its a .html file which includes {{variable}} and controller {% %}
          {%if %}--{% endif %}; {%for in in list%}--{% endfor %}; {% for key, value in dict.iteritems()%}--{% endfor %}
          # and template must saved in 'templates.dir'

Jinjia2: like the frameworks of Web， there are many frameworks of templete,
         and different template has different controller

render:  according to template and variable, create .html file
         render_template('view.html', variable = value)
'''
from flask import Flask, render_template, request

app = Flask(__name__)

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