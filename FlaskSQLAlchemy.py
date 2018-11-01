from string import Template
from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

'''
1. Create database link (named 'engine'), and based on this create a 'Session'
       app.config['SQLALCHEMY_DATABASE_URI'] = address  
       app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
       db = SQLALCHEMY(app)
       
       address = mysql+mysqlconnector://username:password@host:port/database
               = sqlite:///abspath
'''
address = Template('${DataBase_Type}+${Driver}://${Username}:${Password}@${Host}:${Port}/${Database}')
config = {
    'DataBase_Type':'mysql',
    'Username':'root',
    'Password':'123456',
    'Host':'localhost',
    'Port':'3306',
    'Database':'test',
    'Driver':'mysqlconnector'
}
address = address.substitute(**config)

# basedir = os.path.abspath(os.path.dirname(__file__))
# address = 'sqlite:///' + os.path.join(basedir,'test.db')

app.config['SQLALCHEMY_DATABASE_URI'] = address
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
print(address)

'''
 2. Define our object('table') by inheriting from the determined 'Base' class
       Base = declarative_base()
       #1. normal table
       class myTable(Base):
            __tablename__ = 'tablename'
            key1 = Colum(Type, [primary key/unique/nullable], index=)

       #2. Foreign key
           # one to more
           from sqlalchemy.orm import relationship
           from sqlalchemy import ForeignKey

           class Parent(Base):
              __tablename__ = 'parent'
              id = Column(Integer, primary_key=True)
              name = Column(String(20))
              child = relationship('child', backref='parent')

           class Child(Base):
               __tablename__ = 'child'
               id = Column(Integer, primary_key=True)
               name = Column(String(20))
               parent_id = Column(Integer, ForeignKey('parent.id'))

           # more to one
           class Parent(Base):
               __tablename__ = 'parent'
               id = Column(Integer, primary key = True)
               name = Column(String)

           class Child(Base):
              __tablename__ = 'child'
              name = Column(String)
              parent_id = Column(Integer, ForeignKey('parent.id'))
              parent = relationship('parent', backref='child')
'''
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    users = db.relationship('User', backref = 'role')

    def __repr__(self):
        return '<Role %r>' % self.name

    __str__ = __repr__

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return  '<User %s>' % self.username
    __str__ = __repr__


db.create_all()

admin_role = Role(id = 1,name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')
user_john = User(username='john', role = admin_role)
user_susan = User(username='susan', role = user_role)
user_david = User(username='david', role = user_role)

db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_david])