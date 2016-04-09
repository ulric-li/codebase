#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Python的MySQL驱动来连接到MySQL服务器的模块，在debian下可以通过aptitude search mysql | grep python命令搜索到，然后用aptitude install 模块名来安装

网上有教程，安装命令为：pip install mysql-connector-python --allow-external mysql-connector-python

'''


########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector

# change root password to yours:
conn = mysql.connector.connect(user='root', password='Iloveyoubaby2', database='test')

cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()
