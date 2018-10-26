'''
ORM: Object-Relational Mapping   # user table<-->ORM<--> User('1','xzq')
     sqlalchemy is a ORM framework, by using 'Session' complete the information exchanges between 'table' and 'Object'
'''
'''
       # if the table not exist, we should create the table
       Base.metadata.create_all(engine)  # will create all define table
       # if the table has existed, we could operate without create

    3. operation
       insert, query***, revise, delete
'''
from string import Template
from sqlalchemy import create_engine, Column, Integer, String, DATE, FLOAT, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 1. configure, create_engine and make_session
'''
1. Create database link (named 'engine'), and based on this create a 'Session'
       # mysql
       engine = create_engine('DatabaseType+Driver://user:password@host:port/Database')
       # sqlite
       engine = create_engine('sqlite:///path+database.db')

       DBSession = sessionmaker(bind = engine)
'''
engine = Template('${Database_Type}+${Driver}://${user}:${password}@${host}:${port}/${Database}')
config = {
    'Database_Type': 'mysql',
    'Driver': 'mysqlconnector',
    'user': 'root',
    'password': '123456',
    'host': '127.0.0.1',
    'port': '3306',
    'Database': 'test'
}
engine = engine.safe_substitute(**config)
engine = create_engine(engine)
DBsession = sessionmaker(engine)

# 2. define Table(object) and init_db
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
Base = declarative_base()


class User(Base):  # the follow table
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    role_id = Column(Integer, ForeignKey('role.id'))

    def __repr__(self):
        return '<User %r>' % self.name

    __str__ = __repr__


class Role(Base):  # the main table
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, index=True)
    user = relationship('user', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

    __str__ = __repr__


def init_db():
    Base.metadata.create_all(engine)  # will create the no existed table


def drop_db():  # sqlalchemy can't alter table, so if want to alter ,just can drop all tables and revise them.
    Base.metadata.drop_all(engine)  # will drop all tables


init_db()
# drop_db()


# 3. operation with 'Session'
session = DBsession()
'''
# insert into table
new_user = User(id=10,name='Cindy')
new_role = Role(id=11,name='ly')
session.add_all([new_user,new_role])
session.commit()
'''

# query the table
'''
单表查询
view = session.query().filter(condition).order_by(col.[desc()/asc()]).limit(max).[all()/one()/first()]

#      SELECT * FROM table_name [ORDER_BY] col [DESC/ASC] [LIMIT 0, MAX] WHERE [CONDITION]
query() # select * from
filter(condition1 and/or condition2) # where condition1 and or condition2  
order_by(col.[desc()/asc()])  # order_by col [desc/asc]
limit(max)               # select max
all()/one()/first()      # return all/one/first of the object list     

单表聚合
from sqlalchemy import func
view = session.query(col, func.count('*').label('new_name')).filter(condition).group_by(col).[all()/one()/first()]
                              .sum(col)
                              .max(col)/min(col)   
# SELECT col, fun(col) FROM table_name [WHERE CONDITION][GROUP BY] col  
'''
# from sqlalchemy import func
# user = session.query(User.name, User.id, func.count('*').label("user_count")).group_by(User.name, User.id).paginate(User.id > 6)
# for i in user:
#     print(i.name,i.id, i.user_count)


'''
revise:  1. query to get the object to be revised
         2.  object.attr = new_value
         3. session.commit()
'''

'''
delete: 1. query to get the object to be delete
        2. session.delete(object)
        3. session.commit()
'''

# import os
# from sqlalchemy import Column, String, create_engine
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy.ext.declarative import declarative_base
#
# basedir = os.path.abspath(os.path.dirname(__file__))
# engine = create_engine('sqlite:///'+os.path.join(basedir,'test.db'))
# DBSession = sessionmaker(engine)
#
# Base = declarative_base()
#
# class User(Base):
#     __tablename__ = 'user'
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#
# class Book(Base):
#     __tablename__  = "book"
#     id = Column(String(20), primary_key=True)
#     book_name = Column(String(20))
#
# new_user = User(id='6',name='xzq')
# new_book = Book(id='1',book_name='Cindy')
# session = DBSession()
# session.add_all([new_user,])
# session.commit()
# session.close()
#
# session = DBSession()
# user = session.query(User).filter(User.id == '1').one()
# print(user.name)