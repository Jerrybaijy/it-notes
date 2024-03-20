# python连接数据库


# 1.第三方模块pymysql已添加，并引入pymysql
import pymysql

# 2.连接数据库
# 已使用Navicat创建数据库
host = "localhost"  # 主机地址，如果要连接远程数据库，需填写对应数据库地址
port = 3306  # 端口号，注意数字是整型
user = "root"
password = "123456"
db = "51db"  # 数据库名称
charset = "utf8"  # 文件编码

# 3.创建数据库连接对象，并建立连接
db = pymysql.Connect(host = host, port = port, user = user, passwd = password, db = db, charset = charset)
print("数据库已连接.....")

db.close()  # 关闭数据库连接
