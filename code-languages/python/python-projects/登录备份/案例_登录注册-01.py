users_list = [{"name": "zhangsan", "password": "123"}]


def register():
    for user_exist in users_list:
        name = input("请输入注册用户名/退出请按Q：")
        if name.upper() == "Q":
            return  # 输入 Q 退出脚本
        password = input("请输入注册密码：")
        user = {"name": name, "password": password}
        if user["name"] == user_exist["name"]:  # 判断用户名已存在
            print("用户名已存在，请重新输入！")
            continue
        else:
            users_list.append(user)
            print("恭喜你，注册成功！")
            return


def login():
    msg = 0
    while True:  # 循环登录
        name = input("请输入登录用户名/退出请按'Q'：")
        if name.upper() == "Q":
            return
        password = input("请输入登录密码：")
        for user_exist in users_list:
            if name == user_exist["name"] and password == user_exist["password"]:
                print("恭喜你，登录成功！")
                msg = 1
                return msg
        if msg == 0:
            print("用户名密码错误，请重新输入！")
            continue


def user_info():
    print(users_list)


def main():
    while True:
        if login() == 1:  # 登录并判断登录结果
            while True:
                print("-----业务选择------")
                print("1.注册")  # 可以将此类整合到mapping中，通过函数输出
                print("2.登录")
                print("3.查看用户信息")
                print("4.退出")
                choice = input("请选择业务编号：")

                mapping = {
                    "1": register,
                    "2": login,
                    "3": user_info
                }
                func = mapping.get(choice)  # func 即为 mapping 里的值，如果不能获取到键，func 为 None
                if func:  # 即 func 不为 None，能获取键
                    func()  # func 为 mapping 里对应 choice 的值
                elif choice == "4":
                    return  # 函数终止
                else:
                    print("输入错误，请重新选择！")
                    continue
        else:
            break  # 结束外层循环，保证在 login 页面系统可以退出


if __name__ == '__main__':
    main()
