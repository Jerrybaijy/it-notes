# 函数_路径
import os

# 获取路径
file_path1 = os.path.join("python", "Python笔记2", "7.1.模块_时间处理.py")  # 路径拼接  <class 'str'>

abs_path = os.path.abspath(__file__)  # 获取当前文件绝对路径  <class 'str'>

father_path = os.path.dirname(__file__)  # 获取当前文件父级目录  <class 'str'>

base_dir = os.path.dirname(os.path.abspath(__file__))  # 获取当前文件绝对路径的父级目录  <class 'str'>
file_path = os.path.join(base_dir, "a1.txt")  # 获取到当前具体文件的绝对路径


# 判断路径是否存在
res = os.path.exists("path")  # True/False  if not os.path.exists("path"):

# 创建文件夹
os.makedirs("folder_path")