#if-else语句：单个条件判断

# money=120
# if money>=100: #等同于如果，不要忘记冒号
#     print("恭喜你！可以买宝马了！") #print前默认空出一个tap键的距离，表示与if的从属关系
#     print("真开心！") #注意同一条件下的所有print缩进要统一
# else: #等同于否则，不要忘记冒号，且冒号后面没有条件
#     print("努力赚钱吧！") #print前默认空出一个tap键的距离
# print("程序结束!") #此处print前与if缩进一致，不受条件限制一定会执行



#elif多条件判断
#基础示例
# money=120
# if money>=100:
# 	print("可以买宝马了！")
# 	print("真开心！")
# if money>=50 and money<100: #多个条件的if缩进相同
#     print("买丰田！")
# if money>=20 and money<50:
#     print("二手车！")
# else:
#     print("骑共享单车") #此处else只与最近的if起作用，即当money=120的时候，获取结果既有买宝马又有骑共享单车。

#升级示例
# money=120
# if money>=100:
# 	print("可以买宝马了！")
# 	print("真开心！")
# elif money>=50: #缩进与同级别if相同，将多个条件构成一个整体
#     print("买丰田！")
# elif money>=20:
#     print("二手车！")
# else:
#     print("骑共享单车")
#此程序运行结果为：可以买宝马了    真开心
# 关键点：
# if在开头，只有一个，不可省略
# elif可以有任意个
# elif多条件判断中，只执行第一个满足条件的语句，不必考虑前面的if是否会执行
# 缩进与同级别if相同，将多个条件构成一个整体
# else只有末尾一个，可以省略



#选择结构嵌套

# money=int(input("请输入存款金额（万）？"))
# day=int(input("今天是星期几（1-7）？"))
# if money>=100:
# 	print("可以买宝马了！")
# 	print("真开心！")
# 	if day<=5: #此处的if在第一个if与其它elif的基础下，所以缩进要降一个等级
# 		print("周末去提车！")
# 	else: #此处的else在第一个if与其它elif的基础下，与第二个if同级
# 		print("今天下午就去提车！")
# elif money>=50:
#     print("买丰田！")
# elif money>=20:
#     print("二手车！")
# else:
#     print("骑共享单车")


#注意事项：
#条件后的冒号不要掉
#else后面不要写条件
#缩进必须一致

# if 5>3:
# 	print("你好！北京！")
# 	print("你好！北京！")
# 	print("你好！北京！")
# 	print("你好！北京！")
