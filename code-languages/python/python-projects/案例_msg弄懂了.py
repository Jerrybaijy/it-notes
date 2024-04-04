f = open(r"user000.txt", "ab")
while True:
    msg = 1
    name = input("请输入用户名：")
    pwd = input("请输入密码：")
    email = input("请输入邮箱：")
    user = {"用户名":name, "密码":pwd, "邮箱":email}
    line = "{}\n".format(user)
    data = line.encode("utf-8")

    f.write(data)

    print("注册成功！")
    while True:
        choice = input("继续请按1，结束请按2：")
        if choice == "1":
            msg = 1
            break
        if choice == "2":
            msg = 0
            break
        else:
            print("输入错误！")
    if msg == 0:
        break
f.close()
print("----继续执行---")
print("----继续执行---")
print("----继续执行---")