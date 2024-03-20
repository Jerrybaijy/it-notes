#内置模块urllib(爬虫模块)
#爬虫:爬取互联网数据的程序
from urllib import request

url="http://www.baidu.com" #注意https:和http:
data=request.urlopen(url).read() #data为变量，发送请求并读取数据
print(data.decode())  #decode()解码：将二进制转换成字符，此行可以没有

with open(r"8888.html","wb") as f: #f为变量，创建一个文件，等待写入
	f.write(data) #将data获取到的数据写到f中













