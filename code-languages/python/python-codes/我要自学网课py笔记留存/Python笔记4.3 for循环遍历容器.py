#for循环遍历容器    遍历:将容器中的数据一个一个获取出来

#1、直接遍历
# names=["张三","李四","王五","赵六"]
# for name in names:
# 	if name=="王五":
# 		print("有这个人 王五")

#2、构造索引遍历
#2.1遍历列表
# names=["张三","李四","王五","赵六"]
# for i in range(0,len(names)):
# 	print(names[i])

#2.2遍历元组
# scores=(67,78,56,89,76,79,98,45,65,76)
# for i in range(0,len(scores)):
# 	print(scores[i])

#求和并获取平均分
# scores=(67,78,56,89,76,79,98,45,65,76)
# total=0 #提前定义分数
# for score in scores:
# 	total=total+score #每拿到一个分数，都加到total里
# print(total/len(scores))




# #循环遍历字典，只获取键
# dicta={"name":"zhangsan","age":18,"hobby":"play ball"}
#
# for x in dicta:
# 	print(x,dicta[x])



# seta={1,23,232,43,345,46,56}
# for x in seta:
# 	print(x) #集合，无序打印

