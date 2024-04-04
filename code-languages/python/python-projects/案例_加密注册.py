import hashlib

# 输入
user = input("请输入用户名：")
pwd = input("请输入密码：")

# 加密密码
obj = hashlib.md5("88888".encode('utf-8'))  # 88888 加盐
obj.update(pwd.encode('utf-8'))  # 括号里必须是字节
pwd_md5 = obj.hexdigest()

# 写入文件
with open("db.txt", 'a', encoding = 'utf-8') as f:
    line = "{}|{}\n".format(user, pwd_md5)
    f.write(line)