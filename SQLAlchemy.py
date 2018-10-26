'''
ORM: Object-Relational Mapping   # user table<-->ORM<--> User('1','xzq')
     sqlalchemy is a ORM framework, by using 'Session' complete the information exchanges between 'table' and 'Object'
     Flow:
     1. Create database link (named 'engine'), and based on this create a 'Session'
       # mysql
       engine = create_engine('DatabaseType+Driver://user:password@host:port/Database')
       # sqlite
       engine = create_engine('sqlite:///path+database.db')

       DBSession = sessionmaker(bind = engine)
     2. Define our object('table') by inheriting from the determined 'Base' class
       Base = declarative_base()
       class myTable(Base):
            __tablename__ = 'tablename'

            key1 = Column(DataType(Length), primary key = True)
            key2 = Colunm(DataType(Length))
            key3 = relationship('OtherTable')  # foreign key

    3. input 'myTable' into database, through 'Session'
       mytable = myTable(key1=value1, key2=value)
       session = DBSession()
       session.add(mytable)
       session.commit()
       session.close()
    4. get the information of table from database, through 'Session'
       session = DBSession()
       mytable = session.query(myTable).filter(myTable.key==value).one()  # or all()
       key = mytable.key
       value = mytable.value
       session.close()
'''
# # import sqlalchemy:
# from sqlalchemy import Column, String, create_engine
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy.ext.declarative import declarative_base
#
# # create database link: 'DatabaseType+Driver://user:password@host:port/Database'
# engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
# # based on the database, build a 'Session':
# DBSession = sessionmaker(bind=engine)
#
# # Base class of Object:
# Base = declarative_base()
#
# # define our object of table:
# class User(Base):
#     # table name:
#     __tablename__ = 'user'
#
#     # table structure:
#     id = Column(String(20), primary_key=True) # primary key
#     name = Column(String(20))
#     # book = relationship('Book')  # foreign key
#
#
#
# # create 'Session' object:
# session = DBSession()
# # create 'User' object:
# new_user = User(id='2', name='Bob')
# # add into 'Session':
# session.add(new_user)
# # 'Session' commit to the database:
# session.commit()
# # close 'Session':
# session.close()
#
#
# session = DBSession()
# # Query， 'filter' like 'where condition', 'one()' return the only one line, 'all()' return all lines include 'condition':
# user = session.query(User).filter(User.id=='5').one()
# # get the information of 'table' by using 'User' object:
# print('type:', type(user))
# print('name:', user.name)
# session.close()

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