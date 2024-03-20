#服务端：接收客户端消息并显示  先启动服务端
from socket import *
import time

#创建socket对象
s=socket(AF_INET,SOCK_DGRAM) #网络选择IPV4  网络协议UDP（无需连接）

#绑定端口
s.bind(("localhost",3435)) #IP地址  端口号

#接收信息
while 1==1:
	msg=s.recv(1024) #接收，最大字节数1024
	print("----:",msg.decode()) #接收内容  解码


s.close()