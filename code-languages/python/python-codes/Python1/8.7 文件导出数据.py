import pymysql
from pymysql.cursors import DictCursor

# 已创建数据库和数据表(id, username, password, mobile)
# 已创建txt文件（zhangsan, 123, 19999...）
# 连接MySQL
conn = pymysql.Connect(
    host = "localhost",  # 主机地址，如果要连接远程数据库，需填写对应数据库地址
    port = 3306,  # 端口号，注意数字是整型
    user = "root",
    password = "123456",
    charset = "utf8",  # 文件编码
    database = "demo"  # 可提前连接某个特定数据库，以减少后期进入数据库的步骤
)
print("MySQL已连接.....")
cursor = conn.cursor(cursor = DictCursor)

# 执行sql（不要直接字符串格式化）
sql = "select id, username, password, mobile from demo1"
cursor.execute(sql)
user_list = cursor.fetchall()  # [{},{}...]

# 关闭连接
cursor.close()
conn.close()




for user in user_list:
    line = "{}, {}, {}\n".format(user['username'], user['password'], user['mobile'])
    with open('user1.txt', mode = 'a', encoding = 'utf-8') as f:
        f.write(line)
        print("导出")


print("数据导出成功！")
