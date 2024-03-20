# 从汽车之家下载一张图片
import requests

url = " https://club2.autoimg.cn/album/g26/M0A/2C/E9/userphotos/2023/09/03/22/820_ChxkjmT0lFqAcBBbAAvcbidXiqQ277.jpg"
res = requests.get(url)
data = res.content  # 解码

f = open("Benz.png", "wb")
f.write(data)
f.close()
