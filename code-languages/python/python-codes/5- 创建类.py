# 1.创建类
class Cat:  # calss 类名:，类名首字母最好大写，以便与对象重复
  # 1.1初始化方法，即定义属性
  # def __init__(self,属性1, 属性2, 属性3,…)，属性为形参
  # self关键词：在类的内部表示当前对象，即类以内的所有对象
  def __init__(self, nick, color, age):  # 定义属性：昵称，颜色，年龄

    # 给对象的属性赋值，赋的值就是类的属性
    self.nick = nick
    self.color = color
    self.age = age
    self.strain = "加菲猫"  # 内部定义固定属性，所有对象的strain都是加菲猫

  # 1.2其它方法
  # def 方法名(self):  # 每个函数中都有固定参数self
  def eat1(self):
    print("猫在吃鱼！")

  def eat2(self):
    print(self.nick, "猫在吃鱼！")

  # 运行cat2.eat3()  nick(cat2的属性值)在吃鱼！

  def eat3(self, count):
    print(self.nick, "猫在吃鱼！吃了", count, "条鱼！")

  # 运行cat2.eat3(count)  nick(cat2的属性值)在吃鱼！吃了count条鱼！

  def sleep(self):
    print("猫在睡觉！")


# ----------------------------------------
# 2.创建对象(实例化)
# 2.1创建对象名  对象名=类名(属性值1,属性值2,属性值3)，属性值为实参
cat1 = Cat("小苗", "白色", 2)
cat2 = Cat("小黑", "黑色", 1)

# 2.2.获取某个对象的属性   对象名.属性名
print(cat1.nick)
print(cat2.strain)

# 2.3.通过某个对象调用方法  对象名.方法名()
cat1.eat()
cat2.sleep()

print(cat2)
