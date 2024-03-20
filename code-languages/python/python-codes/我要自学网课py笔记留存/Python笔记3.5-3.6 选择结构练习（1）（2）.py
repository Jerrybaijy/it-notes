# #选择结构练习
# 练习1.根据用户输入星期几，输出特价菜是什么？
# 星期一特价菜：水煮鱼
#   星期二特价菜：烧排骨
#   星期三，四特价菜：宫爆鸡丁
#   星期五，六特价菜：清蒸鲈鱼
#   其它：干锅肥肠

# day=int(input("请输入星期几？（1-7）"))
# if day==1:
#     print("星期一特价菜：水煮鱼")
# elif day==2:
#     print("星期二特价菜：烧排骨")
# elif day==3 or day==4:
#     print("星期三、四特价菜：宫爆鸡丁")
# elif day==5 or day==6:
#     print("星期五、六特价菜：清蒸鲈鱼")
# else:
#     print("星期日特价菜：干锅肥肠")


# 练习2.根据输入判断学生的成绩等级，
# 如果成绩>=90分，则输出“优秀”;
# 如果成绩>=80分，则输出“良好”;
# 如果成绩>=60分，则输出“中等”;
# 否则，输出“差”

# score=int(input("请输入考生成绩："))
# if score>=90:
#     print("优秀")
# elif score>=80:
#     print("良好")
# elif score>=60:
#     print("中等")
# else:
#     print("差")


# 练习3.现在有一个银行保险柜，有两道密码。想拿到里面的钱必须两次输入的密码都要正确。
# 如果第一道密码都不正确，那直接把你拦在外面；
# 如果第一道密码输入正确，才能有权输入第二道密码。
# 只有当第二道密码也输入正确，才能拿到钱！(两道密码自己设)(嵌套if)

# 练习3.1没有首先定义密码
password1 = int(input("请输入第一道密码："))
if password1 == 123:
    password2 = int(input("请输入第二道密码："))
    if password2 == 456:
        print("Success!")
    else:
        print("Fail!")
else:
    print("Fail!")

# 练习3.2首先定义密码
# password1=123
# password2=456
# pwd1=int(input("请输入第一道密码："))
# if pwd1==123:
#     pwd2 = int(input("请输入第二道密码："))
#     if pwd2==456:
#         print("Success!")
#     else:
#         print("Fail!")
# else:
#     print("Fail!")


# 练习3.3转换为字符串
# password1=str(input("请输入第一道密码："))
# if password1=="123":
#     password2=str(input("请输入第二道密码："))
#     if password2=="456":
#         print("Success!")
#     else:
#         print("Fail!")
# else:
#     print("Fail!")


# 练习3.4分步提醒
# password1=int(input("请输入第一道密码："))
# if password1==123:
#     print("恭喜你，第一道密码输入正确")
#     password2=int(input("请输入第二道密码："))
#     if password2==456:
#         print("Success!")
#     else:
#         print("Fail!")
# else:
#     print("Fail!")


# 练习3.5老师答案
# password1="123"
# password2="abc"
#
# pwd1=input("请输入第一道密码：")
# if pwd1==password1:
# 	print("第一道密码输入正确！")
# 	pwd2=input("请输入第二道密码：")
# 	if pwd2==password2:
# 		print("恭喜你，输入正确！拿到5毛钱！")
# 	else:
# 		print("很遗憾！第二道密码错误！")
# else:
# 	print("第一道密码输入错误，请出去吧！")


# 练习4.开发一个计算器，用户输入第一个数、加减乘除、第二个数，控制台显示计算结果。

# a=int(input("请输入第一个数字："))
# b=int(input("请输入第二个数字："))
# c=input("请输入+-*/：")
# d=1
# msg=1
# if c=="+":
#     d=a+b
# elif c=="-":
#     d=a-b
# elif c=="*":
#     d=a*b
# elif c=="/":
#     d=a/b
# else:
#     msg=0
#     print("没有这个计算方式")
# if msg==1:
#     print("计算结果：",d)
