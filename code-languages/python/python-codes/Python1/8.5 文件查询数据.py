import pymysql
from pymysql.cursors import DictCursor

# 已创建数据库和数据表(id, username, password, mobile)
while True:
    user = input("用户名：")
    if user.upper() == "Q":
        break

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
    sql = "select*from demo1 where username=%s"
    cursor.execute(sql, [user])
    data = cursor.fetchone()
    print(data)








    cursor.close()
    conn.close()