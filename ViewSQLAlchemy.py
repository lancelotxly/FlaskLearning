from string import Template
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import  DataRequired

app = Flask(__name__)

DataBase_Address = Template('${Database_Type}+${Driver}://${Username}:${Password}@${Host}:${Port}/${Database_Name}')
config = {
    'Database_Type':'mysql',
    'Driver':'mysqlconnector',
    'Username':'root',
    'Password':'123456',
    'Host':'127.0.0.1',
    'Port':'3306',
    'Database_Name':'test'
}
engine = DataBase_Address.substitute(**config)

app.config['SECRET_KEY'] = 'HARD TO GUESS'
app.config['SQLALCHEMY_DATABASE_URI'] = engine
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    users = db.relationship('User',backref = 'role')

    def __repr__(self):
        return '<Role %r>' % self.name
    __str__ = __repr__

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return  '<User %r>' % self.name
    __str__ = __repr__

def Init_DB():
    db.create_all()

def Drop_DB():
    db.drop_all()

Init_DB()

class NameForm(FlaskForm):
    name = StringField('What is your name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def ViewSQLAlchemy():
    form = NameForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter_by(username = form.name.data).first()  # query data where username equal the name of form
        if user is None:     # if the username not exist, insert the username into the User table, and mark with 'know: False' in session
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['know'] = False
        else:
            session['know'] = True
        session['name'] = form.name.data  # save the name into session before redirection
        return redirect(url_for('ViewSQLAlchemy'))
    return render_template('ViewSQLAlchemy.html', form = form, name = session.get('name'), know = session.get('know'))

if __name__ == '__main__':
    app.run()