# 函数_动态参数
# 动态传参：多个位置传参
def func(*args):  # 在形参前面加*，可传多个参数
    return args  # 返回参数


res = func(45, "hj")
print(res)  # (45, 'hj')  得到元组
print(type(res))  # <class 'tuple'>
print(res[0])  # 45  索引元组

res2 = func()
print(res2)  # ()  不传参数得到空元组
print(type(res2))  # <class 'tuple'>


# 动态传参：关键字传参
def func(**kwargs):  # 在形参前面加**，可传多个赋值参数
    return kwargs  # 返回参数


res = func(v1 = 1, v2 = 2)
print(res)  # {'v1': 1, 'v2': 2}  得到字典，v1/v2为键，1/2为值
print(type(res))  # <class 'dict'>
print(res["v1"])  # 1  根据键获得值

res2 = func()
print(res2)  # {}  不传参数得到空字典
print(type(res2))  # <class 'dict'>


# 动态传参：位置和关键字混合传参
def func(*args, **kwargs):  # 混合动态形参
    return args, kwargs  # 返回参数


res = func(11, 22, v1 = 1, v2 = 2)
print(res)  # ((11, 22), {'v1': 1, 'v2': 2})  得到元组
print(type(res))  # <class 'tuple'>
print(res[0])  # (11, 22)  索引元组

res2 = func()
print(res2)  # ((), {})  不传参数得到以空元祖和空字典为元素的元组
print(type(res2))  # <class 'tuple'>
print(res2[0])  # ()  索引元组
