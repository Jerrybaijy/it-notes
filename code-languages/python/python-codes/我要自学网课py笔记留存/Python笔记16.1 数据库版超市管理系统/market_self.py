# 编写业务方法
import orm_self
import random


# 查看商品列表
def get_all_products():
    sql = "SELECT * FROM products;"
    data = orm_self.get_data(sql)
    print("序号    编号    名称    单价   折扣")
    for product in data:
        for x in product:
            print(x, end = "    ")
        print()  # 换行


# 根据编号查询商品
def get_product():
    num = input("请输入商品编号：")
    sql = "SELECT * FROM products WHERE num=" + num + ";"
    data = orm_self.get_data(sql)
    if data != None:
        print("-----商品名称：", data[0][2], "单价：", data[0][3], "折扣：", data[0][4])
        return data[0][2], data[0][3], data[0][4]
    else:
        print("-----商品不存在！")
        return None


# 添加商品
def add_product():
    name = input("请输入商品名称：")
    num = str(random.randint(1000, 9999))
    price = input("请输入商品价格：")
    sql = "INSERT INTO products(num,name,price,discount) VALUES(" + num + ",'" + name + "'," + price + ",1);"
    # 由于id自动生成，所以products要指定添加内容
    r = orm_self.write_data(sql)  # 方便查看执行结果
    print(r)


# 根据编号删除商品
def del_product():
    num = input("请输入商品编号：")
    sql = "DELETE FROM products WHERE num=" + num + ";"
    r = orm_self.write_data(sql)
    if r == 0:
        print("删除失败！")
    else:
        print("商品", num, "已删除！")


# 商品打折（修改折扣）
def set_discount():
    num = input("请输入要修改的商品编号：")
    discount = float(input("请输入设置的折扣："))
    if 0.1 <= discount <= 1:
        sql = "UPDATE products SET discount=" + str(discount) + " WHERE num=" + num + ";"
        r = orm_self.write_data(sql)
        if r == 0:
            print("设置失败！")
        else:
            print("商品", num, "折扣设置成功！")
    else:
        print("折扣输入错误！")


# 查看所有订单；
def get_all_orders():
    sql = "SELECT * FROM orders;"
    data = orm_self.get_data(sql)
    print("序号    编号    数量    金额")
    for order in data:
        for x in order:
            print(x, end = "    ")
        print()


# 删除订单；（通过订单号删除）
def del_order():
    num = input("请输入订单编号：")
    sql = "DELETE FROM orders WHERE num=" + num + ";"
    r = orm_self.write_data(sql)
    if r == 0:
        print("删除失败！")
    else:
        print("订单", num, "已删除！")


# 订单统计(总销量，销售额)；
def accord_order():
    sql = "SELECT * FROM orders;"
    data = orm_self.get_data(sql)
    total_count = 0
    total_amount = 0
    for order in data:
        total_count += order[2]
        total_amount += order[3]
    print("总销量", total_count, "件！，销售额", total_amount, "元！")


# 商品结算
def settle():
    order_count = 0
    order_amount = 0
    msg = 0  # 保存订单是否有效，以决定是否生成新订单
    while 1 == 1:
        data = get_product()
        num = int(input("请输入商品数量："))
        if data != None:
            msg = 1
            price = data[1]
            discount = data[2]
            amount = price * num * discount
            order_count += num
            order_amount += amount
            print("当前添加", num, "件！金额", amount, "元！")
        r = input("继续添加请输入1，结算请输入2：")
        if r == "1":
            continue
        else:
            print("--------------------------------------")
            break
    print("****您购买的总数量", order_count, "件！总金额", order_amount, "元！")

    # 添加订单
    if msg == 1:
        oid = str(random.randint(1000, 9999))  # 随机引入编号
        sql = "INSERT INTO orders(num,count,amount) VALUES(" + oid + "," + str(order_count) + "," + str(
            order_amount) + "); "  # 由于id自动生成，所以order要指定添加内容
        orm_self.write_data(sql)
        print("--------添加成功！")
# ----------------------------------------
