# requests爬虫
import requests

# 抓包获取音乐的链接
# url=""
# url=""
url = "https://p-pc-weboff.byteimg.com/tos-cn-i-9r5gewecjs/uuu_265.mp4"

# get()向服务器发送get请求  .content获取二进制数据（.text 获取文本数据）
data = requests.get(url).content

# 写入到本地
with open(r"E:\文件\工作\程序员\python\以后的以后.mp4", "wb") as f:
    f.write(data)
