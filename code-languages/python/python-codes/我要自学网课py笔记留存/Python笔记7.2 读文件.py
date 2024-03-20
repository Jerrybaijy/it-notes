# 1.读文件
# 1.1打开文件
f=r"E:\文件\工作\程序员\python\python2021资料和练习\python2021课程源码\file\再别康桥.txt"
# f为变量名
# 路径加r取消转义

# 1.2得到对象
file=open(f,"r")
# open(文件路径名，访问模式)
# r为访问模式，read

# 1.3读文件接收结果
data=file.read()

# 1.4关闭文件
file.close()
# 关闭文件资源，不关不影响程序运行，但会耗内存


print(data)
print(type(data))

