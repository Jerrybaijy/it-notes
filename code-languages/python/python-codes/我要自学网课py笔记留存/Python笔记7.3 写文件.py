# 2.写文件
# 如果文件不存在，则创建新文件  如果存在，则覆盖写入
# 文件路径必须已经存在
s="你好，长春！"
# S为变量名,既要写入的内容


# 2.2得到对象
file=open(r"E:\文件\工作\程序员\python\python2021资料和练习\python2021课程源码\file\hello0402.txt","w")
# open(文件路径名，访问模式)
# 路径加r取消转义
# w为访问模式，write

# 2.3写入文件
file.write(s)

file.close()


# 3.追加写入
#如果文件不存在，则创建新文件  如果存在，则追加写入
#文件路径必须已经存在
# s="你好，北京！"
# file=open(r"E:\文件\工作\程序员\python\python2021资料和练习\python2021课程源码\file\hello0402.txt","a")   #a----append
# file.write(s)
# file.close()


#文本文件：r w a