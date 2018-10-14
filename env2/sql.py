# usr/bin/python
# coding: UTF-8

import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "db_shane", charset='utf8' )
cursor = db.cursor() # cursor游标对象
sql = "select * from stu "

try:
	cursor.execute(sql) # 执行sql语句
	result = cursor.fetchall() # 获取数据
	for row in result:
		print(row)
except:
	print("Error")

db.close() # 关闭连接
