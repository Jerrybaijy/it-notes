# ...............一、元组...........................
# 元组独有功能
# 元组中元素不支持修改（特殊：元组嵌套容器）

# 元组公共功能
# for循环  len()  多级索引  切片  in包含  嵌套

# ...............二、字典...........................
# 字典独有功能
dicta = {"name": "ZhangSan", "age": 18, "hobby": "playBall"}

# 根据键获取值
v1 = dicta["name"]  # 传统方法
v2 = dicta["XXXX"]  # 输入不存在的键  # 报错
v3 = dicta.get("name")  # 函数方法
v4 = dicta.get("XXXX")  # 输入不存在的键  # None

# 传统方法
for key in dicta:
    print(key)  # 获取键
    print(dicta[key])  # 获取值
    print(key, dicta[key])  # 获取键和值

# 函数方法
for key in dicta.keys():  # 获取键
    print(key)
for values in dicta.values():  # 获取值
    print(values)
for k, v in dicta.items():  # 获取键和值
    print(k, v)

# 其余功能
dicta["sex"] = "男"  # 增加字典元素
dicta["sex"] = "男"  # 增加字典元素  给一个不存在的键赋值
del dicta["hobby"]  # 删除字典元素

# 构造字典
name = "ZhangSan"
age = 18
hobby = "playBall"
info = {"name": name, "age": age, "hobby": hobby}
print(info)  # {'name': 'ZhangSan', 'age': 18, 'hobby': 'playBall'}

# 2.字典公共功能
# for循环  len()  多级索引（用键作索引）  in包含  嵌套
