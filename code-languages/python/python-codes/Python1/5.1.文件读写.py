# 读文件  二进制文件：访问模式为rb，不解码
f = open(r"file.txt", "r", encoding = "utf-8")  # encoding  解码
content = f.read()
f.close()

# 写文件  二进制文件：访问模式为wb/ab，不解码
content = "你好，长春！"
f = open(r"hello0402.txt", "w", encoding = "utf-8")  # encoding  编码
f.write(content)
f.close()

# with open语句  二进制文件：访问模式为rb/wb/ab，不解码
with open(r"file.txt", "r", encoding = "utf-8") as f:
    content = f.read()

with open(r"file.txt", "a", encoding = "utf-8") as f:
    line = "{}|{}\n".format('user', 'pwd_md5')
    f.write(line)

