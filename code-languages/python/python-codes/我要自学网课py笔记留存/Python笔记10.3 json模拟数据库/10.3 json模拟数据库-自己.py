# json 模拟数据库(以下为自己编写，添加循环登录)
import json
# #1.创建数据库
# with open(r"userziji.txt","w") as f:
#     users='[{"uname":"zhangsan","upwd":"123"},{"uname":"lisi","upwd":"123"},{"uname":"wangwu","upwd":"123"}]'
#     f.write(users)

# #2.读数据
def readData():
    with open(r"userziji.txt","r") as f:
        jsonData=f.read()
        userList=json.loads(jsonData)
        return userList

# #3.写数据
def writeData(userList):
    jsonData=json.dumps(userList,ensure_ascii=False)
    with open(r"userziji.txt","w") as f:
        f.write(jsonData)
        print("-----数据写入成功")

# #4.登录
def login():
    userList=readData()
    while 1==1:
        msg=0
        name=input("请输入用户名：")
        password=input("请输入密码：")
        for user in userList:
            if name == user["uname"] and password == user["upwd"]:
                msg=1
                print("登录成功！")
                break
        if msg == 0:
            print("登录失败，请重新输入！")
            continue
        else:
            break
    return msg


# #5.注册
def reg():
    name=input("请添加用户名：")
    password=input("请添加密码：")
    newUser={"uname":name,"upwd":password}
    userList = readData()
    userList.append(newUser)
    writeData(userList)
    print("----添加用户成功！")



# #具体
if __name__ == '__main__':
    reg()