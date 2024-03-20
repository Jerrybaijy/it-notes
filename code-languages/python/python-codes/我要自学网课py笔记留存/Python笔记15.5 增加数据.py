# 增加数据


# ..............前置 连接数据库.............
# 1.第三方模块pymysql已添加，并引入pymysql、random
import pymysql
import random

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

# .............增加数据...............

# 前置：MySQL数据库已创建并使用Python连接，数据库表格已创建
# 创建游标对象（1.执行sql语句，2.处理数据查询结果）
cursor = db.cursor()

for x in range(3, 13):
    num = x  # id
    name = random.choice(["王五", "赵六", "老七", "大宝"])
    age = random.choice([2, 13, 32, 32, 32, 43, 35, 43])

    # 编写增加数据sql语句  拼接时字符串中的单引号需要加上
    # 格式：sql = "INSERT INTO 表格名字 VALUES("+变量1+","+变量2+",...);"
    # 写入sql语句中的内容都应该是字符串
    # 本身不是字符串的，需要用Python方法转换成字符串
    # 本身为字符串时，需要加单引号，单引号是变量名的一部分
    sql = "INSERT INTO stu VALUES(" + str(num) + ",'" + name + "'," + str(age) + ");"

    cursor.execute(sql)  # 执行sql
    db.commit()  # 提交

cursor.close()  # 关闭
db.close()  # 关闭
