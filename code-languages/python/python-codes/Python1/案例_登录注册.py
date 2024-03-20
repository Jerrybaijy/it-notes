# 第一个自主训练

user_list = [{"name": "zhangsan", "password": "123"}]


def register():
    for user_exist in user_list:
        name = input("请输入注册用户名/退出请按Q：")
        if name.upper() == "Q":
            return
        password = input("请输入注册密码：")
        user = {"name": name, "password": password}
        if user["name"] == user_exist["name"]:
            print("用户名已存在，请重新输入！")
            continue
        else:
            user_list.append(user)
            print("恭喜你，注册成功！")
            return


def login():
    msg = 0
    while True:
        name = input("请输入登录用户名/退出请按'Q'：")
        if name.upper() == "Q":
            msg = 0
            return msg
        password = input("请输入登录密码：")
        for user in user_list:
            if name == user["name"] and password == user["password"]:
                print("恭喜你，登录成功！")
                msg = 1
                return msg
        if msg == 0:
            print("用户名密码错误，请重新输入！")
            continue


def user_info():
    print(user_list)


def main():
    while True:
        result = login()
        if result == 1:
            while True:
                mapping = {
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

                func = mapping.get(choice)  # 如果获取不到键，func为None
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
