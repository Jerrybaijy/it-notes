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

# 操作
with open('user1.txt', mode = 'r', encoding = 'utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:  # 表示空行
            continue
        data_list = line.split(",")  # [...]


        # 执行sql（不要直接字符串格式化）
        sql = "insert into demo1(username, password, mobile) values(%s, %s, %s)"
        cursor.execute(sql, data_list)
        conn.commit()
        print("添加")

# 关闭连接
cursor.close()
conn.close()

print("数据添加成功！")