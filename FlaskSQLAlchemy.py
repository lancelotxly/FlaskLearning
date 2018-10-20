'''
Flask-SQLAlchemy
'''
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
# currently file path, like 'os.path.abspath('.')'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    users = db.relationship('User',backref= 'role')

    def __repr__(self):
        return '<Role %r>' % self.name

    __str__ = __repr__


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %r>' % self.username

    __str__ = __repr__

db.drop_all()
db.create_all()
admin_role = Role(name = 'Admin')
mod_role = Role(name = 'Moderator')
user_role = Role(name = 'User')

user_Cindy = User(username='Cindy', role = admin_role)
user_xzq = User(username='xzq', role = user_role)
user_John = User(username='John', role = user_role)

db.session.add_all([admin_role, mod_role, user_role, user_Cindy, user_xzq, user_John])
db.session.commit()

admin_role.name = 'Administrator'
db.session.add(admin_role)
db.session.commit()

db.session.delete(mod_role)
db.session.commit()

role = db.session.query(Role).all()
print(role)

user = db.session.query(User).filter(User.role == user_role).all()
print(user)