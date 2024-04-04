# 调用
import market_self


def main():
    print("***********************超市管理系统*************************")
    print("***********************1.查看商品列表")
    print("***********************2.根据编号查询商品")
    print("***********************3.添加商品")
    print("***********************4.根据编号删除商品")
    print("***********************5.商品打折")
    print("***********************6.查看所有订单")
    print("***********************7.删除订单")
    print("***********************8.订单统计")
    print("***********************9.商品结算")
    print("***********************10.退出")
    print("***********************************************************")
    c = int(input("请选择："))
    if c == 1:
        market_self.get_all_products()
    elif c == 2:
        market_self.get_product()
    elif c == 3:
        market_self.add_product()
    elif c == 4:
        market_self.del_product()
    elif c == 5:
        market_self.set_discount()
    elif c == 6:
        market_self.get_all_orders()
    elif c == 7:
        market_self.del_order()
    elif c == 8:
        market_self.accord_order()
    elif c == 9:
        market_self.settle()
    else:
        print("***********************************************************")


if __name__ == '__main__':
    main()
