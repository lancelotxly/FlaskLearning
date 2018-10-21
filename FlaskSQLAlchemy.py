'''
Flask-SQLAlchemy:
        Flow:
            1. from flask_sqlalchemy import SQLAlchemy
            2. create_engine, make configure
               app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///abspath'  or 'mysql://user:password@host:port/database'
               app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
               db = SQLAlchemy(app)

            3. define our table by inheriting from 'db.Model'
               class myTable(db.Model):
                    pass

            4. exchanging data between 'object' and 'table', through 'db.session'
               db.drop_all()
               db.create_all()   # create tables without data
               new_mytable = myTable()

               # insert
               db.session.all(new_mytable)

               # advised
               new_mytable.key = value
               db.session.all(new_mytable)

               # delete
               db.session.delete(new_mytable)

               # query
               user = db.session.query(User).filter(User.id =='1').one()
               db.session.commit()

            5. close 'db.session'
               db.session.close()
'''
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
# currently file path, like 'os.path.abspath('.')'

app = Flask(__name__)

# configure, like 'create_engine()'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

# define our table(object), by inheriting from 'db.Model'
'''
key-name: db.Column (# object.attr)

key-DataType:  db.Integer(# int); db.Float(# float); db.String(# String); db.Boolean(# bool)
           db.PickeType(all python obj);
key-Type:  primary_key; unique; index; nullable

key-relation: one-to-many
              # one
              class Role(db.Model):
                 #...
                 users = db.relationship('User', backref='role')
              # many
              class User(db.Model):
                #...
                role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
              where 'user' can get their 'role' according to role_id, thus 'role_id' is a 'ForeignKey' of 'User' that connects 'Role'
              and 'role' can get all 'user's which have the 'role', means 'Role' backref 'User.role' into 'User'
              like:       <--->user 1
                     role1<--->user 2
                          <--->user 3
 
'''
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    users = db.relationship('User',backref= 'role')

    def __repr__(self):
        return '<Role %r>' % self.name

    __str__ = __repr__


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String,unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %r>' % self.username

    __str__ = __repr__

db.drop_all()
db.create_all()    # create table 'user' and 'roles' without any data, if the table has existed, no creation.
admin_role = Role(name = 'Admin')
mod_role = Role(name = 'Moderator')
user_role = Role(name = 'User')

user_Cindy = User(username='Cindy', role = admin_role)
user_xzq = User(username='xzq', role = user_role)
user_John = User(username='John', role = user_role)

# the exchange of information between 'object' and 'table' must through 'db.session'
# insert
db.session.add_all([admin_role, mod_role, user_role, user_Cindy, user_xzq, user_John])
db.session.commit()  # until commit the data can be writed into database

# advise
admin_role.name = 'Administrator'
db.session.add(admin_role)
db.session.commit()

# delete
db.session.delete(mod_role)
db.session.commit()

# query
role = db.session.query(Role).all()
print(role)
user = db.session.query(User).filter(User.role == user_role).all()
print(user)