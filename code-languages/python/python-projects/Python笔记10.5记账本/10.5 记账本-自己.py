# 1.引入模块
import json
import datetime
import time


# 2.创建数据库
# d='[{"时间": "2021/03/04 15:20:21", "项目": "收到王敏货款", "金额": 20000, "分类": "收入"}]'
# with open(r"dataziji.txt","w") as f:
# 		f.write(d)



# 3.读数据
def readData():
    with open(r"dataziji.txt","r") as f:
        jsonData = f.read()
    dataList = json.loads(jsonData)
    return dataList

# 4.写数据
def writeData(dataList):
    jsonData = json.dumps(dataList,ensure_ascii=False)
    with open(r"dataziji.txt","w") as f:
        f.write(jsonData)
        print("------数据写入成功！")


# 5.显示账目
def showData():
    sumOut = 0
    sumIn = 0
    dataList = readData()
    print("**************************账单*******************************")
    for data in dataList:
        if data["分类"] == "支出":
            sumOut += data["金额"]
            print(data["时间"], "    ", data["项目"], "    ", data["金额"] * -1)
        else:
            sumIn += data["金额"]
            print(data["时间"], "    ", data["项目"], "    ", data["金额"])
    print("**************************************************************")
    print("**总收入：", sumIn, "元，总开支：", sumOut, "元，结余：", sumIn - sumOut, "元！")

# 6.增加一笔账目
def addData():
    t = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    content = input("请输入项目：")
    amount = float(input("请输入金额："))
    choice = int(input("请选择（1.收入 2.支出）："))
    cla = "支出"
    if choice == 1:
        cla = "收入"
    newData = {"时间": t, "项目": content, "金额": amount, "分类": cla}
    dataList = readData()
    dataList.append(newData)
    writeData(dataList)




# 7.main()
if __name__ == '__main__':
    while 1 == 1:
        showData()
        choice = int(input("----增加项目请按1："))
        if choice == 1:
            addData()
        time.sleep(2)
        print("\n\n\n")