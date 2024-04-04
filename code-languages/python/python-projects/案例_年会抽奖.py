import random

user_list = ["员工-{}".format(i) for i in range(1, 301)]
reward_list = [
    ("三等奖", 5, "ipad"),
    ("二等奖", 3, "iPhone"),
    ("一等奖", 1, "马尔代夫"),
    ("特等奖", 1, "一套房")
]

for title, count, detail in reward_list:
    input("按回车键抽奖！")
    lucky_list = random.sample(user_list, count)
    for name in lucky_list:
        user_list.remove(name)
    message = "恭喜{}获得{}，奖品是{}！".format("、".join(lucky_list), title, detail)
    print(message)
