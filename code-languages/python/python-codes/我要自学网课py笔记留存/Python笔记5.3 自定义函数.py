#自定义函数


# #1.定义一个函数
# def function1():
# 	print("函数function1被执行了！")
# 	print("呵呵！")


# #2.调用函数
# for x in range(100):
# 	function1()



def getSum(a,b): #定义函数格式，def为关键字，getsum为函数名，a和b为变量
	result=a+b #定义函数规则，函数里面定义的变量，在函数外面无法访问到
	print("相加的结果是：",result) #定义函数结果
#-------------------------------------
getSum(4,5) #调用函数，获取结果为：相加的结果是： 9



