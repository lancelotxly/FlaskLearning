'''
Flask-WTF: object-oriented form
'''
'''
object-oriented form: Form(# object of form)
                      wtforms(# a package include many objects of, e.g. <input type='text'>, <button type='submit'>...)

                      from flask_wtf import Form
                      from wtforms import StringField, PasswordField, SubmitField
                      
                      #1. define our Form class
                      class myform(Form):
                         name = StringField('what\'s your name', validators=[checkout_func()]) # <input type='text' name='name' label='what\'s your name'> 
                         submit = SubmitField()  <button type='submit'>
                         
                      e.g. PasswordField()    <input type='password'>
                           RadioField()
                           
                      #2. generate a form instance and transport into the template
                      form = myform()
                        # we can also operate the information of form without resorting to request.form['key'], like
                          name = form.name.data 
                          name_label = form.name.label
                      ...
                      return render_template('index.html', form = form)
                      
                      #3. create our template
                      # normally
                      <form method='post'>
                          <p>{{form.name.label}}</p>
                          <p>{{ form.name() }}</p>
                          <p>{{ form.submit() }}</p>
                      </form>
                      
                      # based on bootstrap
                      {% import 'bootstrap/wtf.html' as wtf %}
                      {{wtf.quick_form(form)}}
                           
'''

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('ok')

@app.route('/', methods=['GET','POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form = form, name = name)

@app.route('/signin', methods=['GET','POST'])
def index2():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index2.html', form = form, name = name)

if __name__ == "__main__":
    app.run()