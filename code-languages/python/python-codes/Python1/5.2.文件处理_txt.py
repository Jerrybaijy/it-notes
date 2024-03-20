# 得到一个txt文件，把文件名和网址为键值对放入一个字典中
#
# file.txt内容
# 123.jpg,汽车,https://club2.autoimg.cn/album/g26/M0A/2C/E9/userphotos/2023/09/03/22/820_ChxkjmT0lFqAcBBbAAvcbidXiqQ277.jpg
# 456.jpg,卡车,https://club2.autoimg.cn/album/g26/M0A/2C/E9/userphotos/2023/09/03/22/820_ChxkjmT0lFqAcBBbAAvcbidXiqQ277.jpg
# 789.jpg,轿车,https://club2.autoimg.cn/album/g26/M0A/2C/E9/userphotos/2023/09/03/22/820_ChxkjmT0lFqAcBBbAAvcbidXiqQ277.jpg

f = open(r"file.txt", "rb")
content = f.read()
f.close()

data_string = content.decode("utf-8")
# 解码，获取到有换行的字符串

data_string = data_string.strip()
# 去除首尾空白行

data_list = data_string.split("\n")
# 去除每行换行符，获取到一个列表
# 每一行字符串作为列表的一个元素

result = {}
for row in data_list:
    # 遍历列表，获取没有换行符的分行字符串

    group = row.split(",")
    # 切割字符串，切割后的每部分作为新列表的元素

    result[group[0]] = group[2]
    # 构造字典

print(result)
