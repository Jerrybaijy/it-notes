# 以下为自己编写，添加循环登录
# 引入模块
import json
import datetime
import time

# 创建数据库
# d1='[{"用户名": "admin", "密码": "123", "姓名": "张三"},{"用户名": "aaa", "密码": "123", "姓名": "李四"}]'
# with open(r"users-ziji.txt","w") as f:
# 		f.write(d1)
#
# d2='[{"编号":1001, "书名": "<红楼梦>", "作者": "曹雪芹", "借出状态": "可借"},\
# {"编号":1002, "书名": "<java教程>","作者": "齐一天", "借出状态": "可借"},\
# {"编号":1003, "书名": "<圣经>","作者": "耶稣", "借出状态": "已借出"},\
# {"编号":1004, "书名": "<李白诗集>","作者": "李白", "借出状态": "可借"}\
# ]'
# with open(r"books-ziji.txt","w") as f:
# 		f.write(d2)

# 读数据
def readUsers():
	with open(r"users-ziji.txt","r") as f:
		jsonData = f.read()
	dataList = json.loads(jsonData)
	return dataList
def readBooks():
	with open(r"books-ziji.txt","r") as f:
		jsonData = f.read()
	dataList = json.loads(jsonData)
	return dataList

# 写数据
def writeUsers(dataList):
	jsonData = json.dumps(dataList,ensure_ascii=False)
	with open(r"users-ziji.txt","w") as f:
		f.write(jsonData)
		print("------数据写入成功！")
def writeBooks(dataList):
	jsonData = json.dumps(dataList,ensure_ascii=False)
	with open(r"books-ziji.txt","w") as f:
		f.write(jsonData)
		print("------数据写入成功！")

# 用户登录
def login():
	while 1 == 1:
		msg = "失败"
		userList = readUsers()
		name = input("请输入用户名：")
		pwd = input("请输入密码：")
		for user in userList:
			if name == user["用户名"] and pwd == user["密码"]:
				msg = "成功"
				print("------登录成功！")
				break
		if msg == "失败":
			print("登录失败，请重新输入！")
			continue
		else:
			break
	return msg

# 1.显示图书列表
def showBooks():
	dataList = readBooks()
	print("----------图书列表----------")
	for book in dataList:
		print(book["编号"],"   ",book["书名"],"   ",book["作者"],"   ",book["借出状态"])
	print("---------------------------")

# 2.图书上架
def addBook():
	dataList = readBooks()
	numList = []
	for book in dataList:
		numList.append(book["编号"])
	newNum = max(numList)+1
	bookName = input("请输入书名：")
	bookName = "<"+bookName+">"
	author = input("请输入作者：")
	state = "可借"
	newBook = {"编号":newNum,"书名":bookName,"作者":author,"借出状态":state}
	dataList.append(newBook)
	writeBooks(dataList)
# 3.图书下架
def delBook():
	dataList = readBooks()
	showBooks()
	data1 = input("请输入图书名：")
	data2 = int(input("请输入图书编号："))
	for book in dataList:
		if data1 == book["书名"] or data2 == book["编号"]:
			dataList.remove(book)
			print("-----图书", book["书名"], "已下架！")
			writeBooks(dataList)
			showBooks()

# 4.借书
def lendBook():
	showBooks()
	msg = 0
	dataList = readBooks()
	num = int(input("请输入要借的图书编号："))
	for book in dataList:
		if num == book["编号"]:
			msg = 1
			if book["借出状态"] == "可借":
				print("----您已成功借出图书：", book["书名"], "！")
				book["借出状态"] = "已借出"
				writeBooks(dataList)
			else:
				print("----", book["书名"], "已经借出！下次再来吧！")
	if msg == 0:
		print("-----没有此图书！")
	showBooks()

# 5.还书
def returnBook():
	showBooks()
	dataList = readBooks()
	num = int(input("请输入要归还的图书编号："))
	msg = 0
	for book in dataList:
		if num == book["编号"]:
			msg = 1
			if book["借出状态"] == "已借出":
				print("----成功归还图书", book["书名"], "!")
				book["借出状态"] = "可借"
				writeBooks(dataList)
			else:
				print("---该图书不允许归还！")
	if msg == 0:
		print("-----没有此图书！")
	showBooks()


# 主函数
def main():
	print("***********************图书管理系统1.0*************************")
	msg = login()
	if msg == "成功":
		while 1 == 1:
			print("1.显示所有图书；\n2.图书上架；\n3.图书下架；\n4.借书；\n5.还书。")
			print("*************************************************************")
			c = int(input("请输入业务编号（1-5）："))
			if c == 1:
				showBooks()
			elif c == 2:
				addBook()
			elif c == 3:
				delBook()
			elif c == 4:
				lendBook()
			elif c == 5:
				returnBook()
			else:
				print("没有此业务！")


# 运行
if __name__ == '__main__':
	main()
	# login()
	# addBook()
	# showBooks()
	# delBook()
	# lendBook()
	# returnBook()
	# pass