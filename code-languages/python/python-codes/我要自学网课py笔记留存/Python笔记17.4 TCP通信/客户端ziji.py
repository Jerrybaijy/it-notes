#客户端：发送消息给服务端，后启动客户端
from socket import *

#创建socket对象
# AF_UNIX  本机通信
# AF_INET  IPV4通信
# AF_INET6  IPV6通信

# SOCK_STREAM  TCP协议
# SOCK_DGRAM  UDP协议

s=socket(AF_INET,SOCK_STREAM) #网络选择  通信协议

#和目标建立连接
s.connect(("localhost",6363)) #客户端和服务端都是本机，所以IP地址为localhost,6363为端口号

#发送消息
s.send("你好！服务端！".encode())  #.encode()对字符串进行编码

#关闭socket
s.close()
