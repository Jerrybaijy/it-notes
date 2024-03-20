# 1.引入pymysql
import pymysql
from pymysql.cursors import DictCursor


# 2.连接MySQL
conn = pymysql.Connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "123456",
    charset = "utf8",
    database = "db1"
)
print("MySQL已连接.....")
cursor = conn.cursor(cursor = DictCursor)


# # 3.查看所有数据库
# cursor.execute("show databases;")
# result = cursor.fetchall()
# print(result)
#
#
# # 4.创建数据库
# cursor.execute("create database db2 default charset=utf8;")
# conn.commit()
# print("创建数据库成功！")
#
#
# # 5.删除数据库
# cursor.execute("drop database db2;")
# conn.commit()
# print("删除成功！")
#
#
# # 6.查询所有数据表
# cursor.execute("show tables;")
# result = cursor.fetchall()
# print(result)
#
#
# # 7.创建数据表
# sql = """
# create table tb3(
# 	id bigint unsigned primary key auto_increment not null,  # 一般以id作为主键
# 	name varchar(16),
#     mobile char(11),
#     email varchar(128),
#     salary decimal(10, 2),
# 	ctime datetime
# )default charset=utf8;"""
# cursor.execute(sql)
# conn.commit()
# print("创建数据表成功！")
#
#
# # 8.删除数据表
# cursor.execute("drop table tb3")
# conn.commit()
# print("删除数据表成功！")
#
#
# # 9.增加数据行
# sql = "insert into tb1(name, mobile, email, salary, ctime) values('zhaoliu', '18888888888', 'x@qq.com', 1000, '2023-11-01 12:30:30');"
# cursor.execute(sql)
# conn.commit()
# print("增加数据行成功！")
#
# # 9.1.增加多行数据行
# sql = """insert into tb1(name, mobile, email, salary, ctime) values
#     ('mayun', '18888888888', 'x@qq.com', 1000, '2023-11-01 12:30:30'),
#     ('zhangsan', '18888888888', 'x@qq.com', 1000, '2023-11-01 12:30:30'),
#     ('lisi', '18888888888', 'x@qq.com', 1000, '2023-11-01 12:30:30');"""
# cursor.execute(sql)
# conn.commit()
# print("增加数据行成功！")
#
#
# # 10.删除数据行
# sql = "delete from tb1 where name='zhangsan';"
# cursor.execute(sql)
# conn.commit()
# print("删除数据行成功！")
#
#
# # 11.删除所有数据行
# cursor.execute("delete from tb1;")
# conn.commit()
# print("删除所有数据行成功！")
#
#
# # 12.查询所有数据
# cursor.execute("select * from tb1;")
# result = cursor.fetchall()
# print(result)
#
# # 12.1.查询特定数据
# sql = "select id from tb1 where name = 'zhaoliu';"
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)
#
# # 12.查询第一行数据
# cursor.execute("select * from tb1;")
# result = cursor.fetchone()
# print(result)
#
#
# # 13.修改数据
# sql = "update tb1 set mobile = '1999998888' where name = 'zhangsan';"
# cursor.execute(sql)
# conn.commit()
# print("修改数据成功！")
#
# # 13.1.修改多个数据（某行）
# sql = """update tb1 set
# 	name = 'zhaoliu',
# 	mobile = '1999999999'
# where name = 'zhangsan';"""
# cursor.execute(sql)
# conn.commit()
# print("修改某行数据成功！")
#
# # 13.2.修改多个数据（某列）
# sql = "update tb1 set mobile = '1999998888';"
# cursor.execute(sql)
# conn.commit()
# print("修改某列数据成功！")



cursor.close()
conn.close()