# 删除和修改数据


# ..............前置 连接数据库.............

import pymysql

# 需要先创建一个数据库，才能连接
host = "localhost"
port = 3306  # 注意使用数字
user = "root"
password = "123456"
db = "51db"  # 数据库名称
charset = "utf8"

# 创建数据库连接对象，并建立连接
db = pymysql.Connect(host = host, port = port, user = user, passwd = password, db = db, charset = charset)
print("数据库已连接.....")

# .............删除和修改数据...............

# 前置：MySQL数据库已创建并使用Python连接，数据库表格已创建，数据已增加
cursor = db.cursor()  # 创建游标对象

# 编写删除数据sql语句  变量值为字符串时需要加单引号
# 格式：sql = "DELETE FROM 表格名 WHERE 变量名 = '变量值'"
# sql = "DELETE FROM stu WHERE name = '大宝'"

# 编写修改数据sql语句  变量值为字符串时需要加单引号
# 格式：sql = "UPDATE 表格名 set 变量名2 = 变量名2的修改 WHERE 变量名 = '变量值'"
sql = "UPDATE stu set age = age + 2 WHERE name='老七'"

cursor.execute(sql)  # 执行sql
db.commit()  # 提交

cursor.close()  # 关闭
db.close()  # 关闭
