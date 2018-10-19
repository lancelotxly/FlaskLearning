import mysql.connector

conn = mysql.connector.connect(user='root', password = '123456', database = 'test')
cursor = conn.cursor()

# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1','Michael'])