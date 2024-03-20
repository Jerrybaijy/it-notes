#服务端：接收客户端消息并显示，先启动服务端
from socket import *

#创建socket对象
s=socket(AF_INET,SOCK_STREAM)

#绑定监听端口
s.bind(("localhost",6363)) #客户端和服务端都是本机，所以IP地址为localhost,6363为端口号

#监听
s.listen()

#等待消息
conn,adr=s.accept() #conn链接对象  adr对方地址

#接收信息
msg=conn.recv(1024) #1024为最大字节数

print("--------:",msg.decode()) #decode 解码

s.close()