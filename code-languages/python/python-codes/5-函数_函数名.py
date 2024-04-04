# 函数名的巧用  函数名也是变量

# 函数名可用其它变量代替
def f():
    print(123)
f()  # 123

f1 = f
f1()  # 123  f1 = f, 故f1() = f()

user_list = [11, "中国联通", (11, 22), f, f()]
user_list[-2]()  # user_list[-2]索引到函数名f，后面加()，整体作为函数名，相当于f()
user_list[-1]  # user_list[-1]索引到函数名f()


# for循环调用多个函数

def send_sms():
    print("发送短信")
def send_email():
    print("发送邮件")
def send_dingding():
    print("发送钉钉")
def send_wechat():
    print("发送微信")
func_list = [send_sms, send_email, send_dingding, send_wechat]  # 注意此处元素没有引号
for func in func_list:
    func()  # 发送短信  发送邮件  发送钉钉  发送微信



# 字典调用多个函数
def register():
    print("运行注册程序")
def login():
    print("运行登录程序")
def user_info():
    print("运行查看用户信息程序")

mapping = {
            "1": register,
            "2": login,
            "3": user_info
        }  # 将函数放入字典
print("1.注册")
print("2.登录")
print("3.查看用户信息")
choice = input("请选择业务编号")
func = mapping.get(choice)  # 如果获取不到键，func为None
if func:
    func()



