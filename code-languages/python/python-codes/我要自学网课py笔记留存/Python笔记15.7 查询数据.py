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

# ..............查询数据.............

# 前置：MySQL数据库已创建并使用Python连接，数据库表格已创建，数据已增加
cursor = db.cursor()  # 创建游标对象

# 编写查询数据sql语句  查询某个对象的某个值
# 格式："SELECT 变量名1 FROM 表格名 WHERE 变量名2 = '变量值2';"
# sql = "SELECT age FROM stu WHERE name = '张三';"

# 编写查询数据sql语句  查询某个对象的所有值
# 格式："SELECT 变量名1 FROM 表格名 WHERE 变量名2 = '变量值2';"
# sql = "SELECT * FROM stu WHERE name = '王五';"

# 编写查询数据sql语句  查询表格内所有对象
# 格式："SELECT * FROM 表格名;"
sql = "SELECT * FROM stu;"

cursor.execute(sql)  # 执行sql 无需提交，提交只在更新操作中使用

# data = cursor.fetchone()  # 获取一行数据,即获取对象的值
data = cursor.fetchall()  # 获取多行数据，即获取对象
print(data)  # 获取data为元组，通过索引获取到具体变量值

cursor.close()  # 关闭
db.close()  # 关闭
