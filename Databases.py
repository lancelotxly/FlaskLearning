'''
sqlite, mysql, sql, mysql-python-connector, orm(SQLAlchemy)
'''

'''
sqlite:  # mostly in ios/android app
      operation flow:
          1. 'Connect'
             conn = sqlite3.connect('test.db')  # if not exists, it will be created
          2. Open the 'Cursor', which can be used to execute 'sql' order
             cursor = conn.cursor()
          3. Execute 'sql' order
             cursor.execute('sql',[value1, value2])   # the placeholder is '?'
          4. After end, close 'Cursor' and commit 'Connect'
             cursor.close()   
             conn.commit()
          5. Before end, close 'Connect'
             conn.close()
             
     tips: Pycharm provide visual operation on Database, if you download derive files and connect to your database
           and you can also directly write 'sql' files to operate the database.         
'''
# import sqlite3
#
# conn = sqlite3.connect('test.db')
#
# cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (?, ?)', ['1','xzq'])
# print(cursor.rowcount)
#
# # Cursor select from tables, and fetchall data. The returned results is a list and every line of the table is a tuple.
# cursor.execute('select * from user where id=?', ['1',])
# values = cursor.fetchall()
# print(values)
#
# cursor.close()
# conn.commit()
#
# conn.close()


'''
mysql:  # create workspace
        #1.  install mysql
        1. write configure file
           [mysql]
           default-character-set = utf-8
           [mysqld]
           port = 3306
           # installation address 
           basedir = D:\\mysql\\mysql-5.7.23-win64
           #  data will be saved in the address
           datadir = D:\\mysql\\mysql-5.7-23-win64\\sqldata
           max_connections = 20
           character-set-server = utf-8
           default-storage-engine = INNODB
        2. initialize
           mysql --initialize -- console
        3. install
           mysql install
           net start mysql
        
        #2. install mysql-connector-python    
        
        # operation flow:
        1. 'Connect'
           conn = mysql.connector.connect(user='', password='', database='')
        2. Open 'Cursor'
           cursor = conn.cursor()
        3. Execute 'sql' order
           cursor.execute('sql',[value1, value2,..])   # placeholder is '%s', '%d'
           
           tips: cursor is just like a IO component,  .py<-->cursor<-->database
                 thus, when .py wants to get information for database, must through 'Cursor'
                 e.g.  Cursor.execute('select sql')
                       values = cursor.fetchall() 
        4. After operation end
           cursor.close()
           conn.commit()
        5. Finally
           conn.close()
'''
# import mysql.connector
#
# conn = mysql.connector.connect(user='root', password = '123456', database = 'test')
#
# cursor = conn.cursor()
#
# cursor.execute('create table user(id varchar(20) primary key , name varchar(20) )')
#
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1','Cindy'])
# print(cursor.rowcount)
#
# cursor.execute('select * from user where id = %s', ('1',))
# values = cursor.fetchall()
# print(values)
#
# cursor.close()
# conn.commit()
#
# conn.close()


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
       key = matable.key
       value = matable.value
       session.close()
'''
# import sqlalchemy:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# create database link: 'DatabaseType+Driver://user:password@host:port/Database'
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
# based on the database, build a 'Session':
DBSession = sessionmaker(bind=engine)

# Base class of Object:
Base = declarative_base()

# define our object of table:
class User(Base):
    # table name:
    __tablename__ = 'user'

    # table structure:
    id = Column(String(20), primary_key=True) # primary key
    name = Column(String(20))
    # book = relationship('Book')  # foreign key



# create 'Session' object:
session = DBSession()
# create 'User' object:
new_user = User(id='2', name='Bob')
# add into 'Session':
session.add(new_user)
# 'Session' commit to the database:
session.commit()
# close 'Session':
session.close()

# 创建Session:
session = DBSession()
# Query， 'filter' like 'where condition', 'one()' return the only one line, 'all()' return all lines include 'condition':
user = session.query(User).filter(User.id=='5').one()
# get the information of 'table' by using 'User' object:
print('type:', type(user))
print('name:', user.name)
session.close()
