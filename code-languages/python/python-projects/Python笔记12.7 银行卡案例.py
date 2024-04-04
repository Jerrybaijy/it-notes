#本节课缺失课件，以下为自己编写

#编写一个银行卡类
#属性：银行名称，卡号，密码，姓名，余额
#方法：登录，存款

#1.创建类
#1.1初始化方法
class Card():
    def __init__(self,cnum,cpwd,cname,cbalance):
        self.bankName = "Python银行"
        self.cnum = cnum
        self.cpwd = cpwd
        self.cname = cname
        self.cbalance = cbalance

#1.2创建方法
    def longin(self):
        unum = input("请输入卡号：")
        upwd = input("请输入密码：")
        if unum == self.cnum and upwd == self.cpwd:
            print("验证成功！")
            return "Ok"
        else:
            print("验证失败！")
            return "No"
    def deposit(self):
        r = self.longin() #类的内部可以调用其它函数
        if r == "Ok":
            money = float(input("请输入存款金额："))
            self.cbalance += money
            print("存款成功！存入",money,"元！余额",self.cbalance,"元！")
# -----------------------------------------------------------
# 2.创建对象
c1 = Card("1001","123","张三",0)
c2 = Card("1002","123","张三",0)

c1.deposit()