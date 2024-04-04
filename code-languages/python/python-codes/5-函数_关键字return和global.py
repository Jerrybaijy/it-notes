# 函数关键字return和global典型示例

# 多个返回值示例：
def func2():
  a = 11
  b = 22
  c = 33
  return a, b, c


r1, r2, r3 = func2()  # 把返回值分别赋值给r1, r2, r3
print(r1, r2, r3)  # 11 22 33
print(r1)  # 11
r4 = func2()  # 把返回值赋值给r4，并放入一个元组中
print(r4)  # (11 22 33)
print(type(r4))  # <class 'tuple'>

# global 典型示例
v1 = 1
v2 = 2
v3 = 3


def func():
  v2 = 3
  global v3
  v3 = 4  # 通过global，将全局变量v3的值改为4
  v4 = 4
  print(v1)  # 1  获取全局变量v1的值
  print(v2)  # 3  获取局部变量v2的值
  print(v3)  # 4  获取全局变量v3的新值
  print(v4)  # 4  取局部变量v4的值


func()  # 1 3 4 4
print(v1)  # 1  获取全局变量v1的值
print(v2)  # 2  获取全局变量v2的值
print(v3)  # 4  获取全局变量v3的新值
print(v4)  # 报错  全局不能直接调用未经全局化的局部变量
