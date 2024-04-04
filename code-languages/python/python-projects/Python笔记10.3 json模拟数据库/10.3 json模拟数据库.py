#json模拟数据库
#在文本文件中保存json字符，通过文件读写来操作数据
import json

# 1.创建数据库
# 创建txt文件，将数据信息以json格式保存在该文件中
#注意使用编程程序创建文本文件，否则会出现编码问题
# with open(r"user.txt","w") as f:
# 	users='[{"uname":"zhangsan","upwd":"123"},{"uname":"lisi","upwd":"123"},{"uname":"wangwu","upwd":"123"}]'
# 	f.write(users)

#2.读数据（查询）
#获取数据库文件中的json数据，转换成Python数据userList，并返回至Python数据
def readData():
	with open(r"user.txt","r") as f:
		jsonData=f.read()
	usersList=json.loads(jsonData)
	return usersList

#3.写数据（修改）
#将新Python数据userList转换成json数据，并写入数据库文件
def writeData(usersList):
	jsonData=json.dumps(usersList,ensure_ascii=False)
	with open(r"user.txt","w") as f:
		f.write(jsonData)
		print("----数据写入成功！")

#4.登录
def login():
	name=input("请输入用户名：")
	password=input("请输入密码：")
	usersList=readData() #读取数据库文件中的json数据，转换成Python数据，详见readData()，并用userList接收
	msg="失败"
	for user in usersList:
		if name==user["uname"] and password==user["upwd"]:
			msg="成功"
			print("----恭喜登陆成功！")
	if msg=="失败":
		print("----登录失败！")
	return msg


#5.注册（在数据库中增加用户）
def reg():
	name=input("请输入新用户名：")
	password=input("请输入密码：")
	newuser={"uname":name,"upwd":password} #新用户
	usersList=readData()#读取数据库文件中的json数据，转换成Python数据，详见readData()，并用userList接收
	usersList.append(newuser) #将新用户添加到Python数据usersList
	writeData(usersList) #将Python数据usersList转换成json数据并写入数据库文件，详见writeData()
	print("-----新用户添加成功！")

#-------------------------
if __name__ == '__main__':
	login()



