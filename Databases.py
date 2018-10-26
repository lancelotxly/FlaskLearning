'''
sqlite, mysql, sqlite, mysql-python-connector
'''
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
           config = {
              'host': '127.0.0.1',
              'port': 3306,
              'user': 'root',
              'password': '123456',
              'database': 'test'
           }
           conn = mysql.connector.connect(**config)

        2. Open 'Cursor'  # cursor is just like a IO component,  .py<-->cursor<-->database
           cursor = conn.cursor()

        3. Execute 'sql' order
           sql=''
           cursor.execute(sql)
           # insert
           sql = 'insert into table_name (id, name) values (%s, %s)'
           cursor.execute(sql,[id, name])
           # select
           sql = 'select..'
           cursor.execute(sql)
           values = cursor.fetchall()   # values is a list of some tuples about the selected information

        4. After operation end
           conn.commit()
        5. Finally
            cursor.close()
            conn.close()
'''
# import mysql.connector
#
# config = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'password': '123456',
#     'database': 'test'
# }
# try:
#     conn = mysql.connector.connect(**config)
#     cursor = conn.cursor()
#     sql_create_table = 'create table if not exists user (id INT(3) primary key, name varchar(20) not null)'
#     cursor.execute(sql_create_table)
#     conn.commit()
#
#     id = 6
#     name = 'xzq'
#     sql_insert = 'insert into user (id, name) values (%s, %s)'
#     cursor.execute(sql_insert, [id, name])
#     conn.commit()
#
#     sql_query = 'select * from user'
#     cursor.execute(sql_query)
#     values = cursor.fetchall()
#     print(values)
# finally:
#     cursor.close()
#     conn.close()

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
             conn.commit()
          5. Before end, close 'Connect'
             cursor.close() 
             conn.close()
             
     tips: Pycharm provide visual operation on Database, if you download derive files and connect to your database
           and you can also directly write 'sql' files to operate the database.         
'''
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (?, ?)', ['1','xzq'])
print(cursor.rowcount)

# Cursor select from tables, and fetchall data. The returned results is a list and every line of the table is a tuple.
cursor.execute('select * from user where id=?', ['1',])
values = cursor.fetchall()
print(values)
conn.commit()

cursor.close()
conn.close()
