# 创建表格


# ............前置 连接数据库..........
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

# ............创建表格.............

# 前置：已使用Navicat创建数据库，并使用Python连接MySQL数据库
# 创建游标对象（1.执行sql语句，2.处理数据查询结果）
cursor = db.cursor()

# 编写sql语句  列名，列数据类型
# 格式：sql = "CREATE TABLE 表格名字(变量1 数据类型,变量2 数据类型,...)"
# stu为表格名字 varchar(10)为长度为10的字符串
sql = "CREATE TABLE stu(id int,name varchar(10),age int)"

# 执行sql
cursor.execute(sql)

# 提交数据
db.commit()

# 关闭游标
cursor.close()

# 关闭数据库连接
db.close()
