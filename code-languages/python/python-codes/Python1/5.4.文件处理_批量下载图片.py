# 要求：得到一个txt文件，根据文件信息将图片批量下载到本地
# 步骤：先用文件名和网址构造字典，再遍历字典下载

# file.txt内容
# 123.jpg,汽车,https://club2.autoimg.cn/album/g26/M0A/2C/E9/userphotos/2023/09/03/22/820_ChxkjmT0lFqAcBBbAAvcbidXiqQ277.jpg
# 456.jpg,卡车,https://club2.autoimg.cn/album/g26/M0A/2C/E9/userphotos/2023/09/03/22/820_ChxkjmT0lFqAcBBbAAvcbidXiqQ277.jpg
# 789.jpg,轿车,https://club2.autoimg.cn/album/g26/M0A/2C/E9/userphotos/2023/09/03/22/820_ChxkjmT0lFqAcBBbAAvcbidXiqQ277.jpg


import requests

# 将文件名和网址信息放入字典，详见《文件处理_txt》
f = open(r"file.txt", "rb")
content = f.read()
f.close()

data_string = content.decode("utf-8")
data_string = data_string.strip()
data_list = data_string.split("\n")

result = {}
for row in data_list:
    group = row.split(",")
    result[group[0]] = group[2]

    # 批量下载  下载图片详见《文件处理_下载图片》
    res = requests.get(group[2])  # group[2]为之前获取到的url
    data = res.content
    f = open(group[0], "wb")  # group[0]为之前获取到的文件名
    f.write(data)
    f.close()
