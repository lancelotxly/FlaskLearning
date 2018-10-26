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

from flask import Flask, render_template, session, redirect, url_for, flash
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

# Form + wtform + bootstrap
@app.route('/', methods=['GET','POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form = form, name = name)

# Form + wtform
@app.route('/signin', methods=['GET','POST'])
def index2():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index2.html', form = form, name = name)

'''
When users flash their browser, the browser will send the last Requestion, 
and if the Requestion is a POST, the browser will alarm you.
tips: don't POST at the last

POST/redirect/GET:
'''
# redirect
@app.route('/user',methods=['GET','POST'])
def index3():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index3'))
    return render_template('index.html', form = form, name = session.get('name'))


'''
flash: flash('information') # to let user know that the status is changed.
       template:  {% for message in get_flashed_message()%}  # get information of flashed
                  {{ message}}
                  {% endfor %}
'''
@app.route('/flash', methods=['GET','POST'])
def indexflash():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name')
        session['name'] = form.name.data
        return  redirect(url_for('indexflash'))
    return render_template('indexflash.html', form = form, name = session.get('name'))
if __name__ == "__main__":
    app.run()