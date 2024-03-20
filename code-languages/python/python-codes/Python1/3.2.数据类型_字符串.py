# 字符串独有功能

data_list = ["张三", "李四", "王五"]
data = "ad min.123"

data.upper()  # 转大写 .lower()  转小写

data.startswith("a")  # True  判断是否以"a"开头   endswith()  结束

data.isdecimal()  # False 判断字符串是不是数字（并非数值）

data.replace("a", "A")  # 替换

data.split(".", maxsplit = 1)  # 保留1个元素切割

"_".join(data_list)  # 连接

data.strip()  # 去除空格/换行  lstrip  去除左侧     rstrip  去右侧除


# 字符串公共功能
# for循环  len(data)  多级索引  切片data[0:3:2]  in包含



