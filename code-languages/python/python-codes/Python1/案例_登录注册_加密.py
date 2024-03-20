import hashlib

USER_FILE_PATH = "user_file.txt"
def md5(data_string):
    obj = hashlib.md5("88888".encode('utf-8'))  # 加盐
    obj.update(data_string.encode('utf-8'))  # 括号里必须是字节
    return obj.hexdigest()  # 返回密文


def register():
    user = input("请输入注册用户名：")
    if user.upper() == "Q":
        return
    pwd = input("请输入注册密码：")
    pwd_md5 = md5(pwd)

    with open(USER_FILE_PATH, 'a', encoding = 'utf-8') as f:
        line = "{}|{}\n".format(user, pwd_md5)
        f.write(line)
    print("恭喜你，注册成功！")


def login():
    msg = 0
    while True:
        user = input("请输入登录用户名/退出请按'Q'：")
        if user.upper() == "Q":
            msg = 0
            return msg
        pwd = input("请输入登录密码：")
        pwd_md5 = md5(pwd)

        with open(USER_FILE_PATH, 'r', encoding = 'utf-8') as f:
            for line in f:
                line = line.strip()
                user_library, pwd_library = line.split('|')
                if user == user_library and pwd_md5 == pwd_library:
                    print("恭喜你，登录成功！")
                    msg = 1
                    return msg
        if msg == 0:
            print("用户名密码错误，请重新输入！")
            continue


def user_info():
    with open(USER_FILE_PATH, 'r', encoding = 'utf-8') as f:
        for line in f:
            print(line)


def main():
    while True:
        result = login()
        if result == 1:
            while True:
                func_dict = {
                    "1": register,
                    "2": login,
                    "3": user_info
                }
                print("-----业务选择------")
                print("1.注册")  # 可以将此类整合到mapping中，通过函数输出
                print("2.登录")
                print("3.查看用户信息")
                print("4.退出")
                choice = input("请选择业务编号：")

                func = func_dict.get(choice)  # 如果获取不到键，func为None
                if func:
                    func()
                elif choice == "4":
                    return
                else:
                    print("输入错误，请重新选择！")
                    continue
        else:
            break  # 保证在login页面系统可以退出


if __name__ == '__main__':
    main()

# 测试
# register()
# login()
# user_info()


