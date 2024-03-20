import pymysql
from pymysql.cursors import DictCursor

# 已创建数据库和数据表(id, username, password, mobile)
while True:
    user = input("请输入用户名：")
    if user.upper() == "Q":
        break
    pwd = input("请输入密码：")
    phone = input("请输入手机号：")

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
    sql = "insert into demo1(username, password, mobile) values(%s, %s, %s)"
    cursor.execute(sql, [user, pwd, phone])
    conn.commit()
    print("数据添加成功！")



    cursor.close()
    conn.close()