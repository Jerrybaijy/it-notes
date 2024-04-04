from datetime import datetime
import time
from datetime import timedelta

time.sleep(2)  # 程序休眠2秒

time_stamp = time.time()  # 获取时间戳  <class 'float'>

time_date = datetime.now()  # 获取当前时间  <class 'datetime.datetime'>

res = datetime.now() + timedelta(days = 50)  # 时间增量  <class 'datetime.datetime'>

# 时间差
# 引入datetime

start_string = "2023-10-18 08:10:08"
start_date = datetime.strptime(start_string, "%Y-%m-%d %H:%M:%S")
end_string = "2024-06-18 16:15:15"
end_date = datetime.strptime(end_string, "%Y-%m-%d %H:%M:%S")
time_delta = end_date - start_date  # 两个时间的差  <class 'datetime.timedelta'>
time_delta_seconds = time_delta.seconds  # 切换成秒  <class 'int'>

# datetime转字符串
# 引入datetime

time_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(time_string)  # 2023-10-18 11:06:11
print(type(time_string))  # <class 'str'>

# 字符串转datetime
# 引入datetime

time_string = "2023-10-18 11:06:11"
time_date = datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print(time_date)  # 2023-10-18 11:06:11
print(type(time_date))  # <class 'datetime.datetime'>

# datetime转时间戳
# 引入datetime

time_stamp = datetime.now().timestamp()
print(time_stamp)  # 1697599215.415559
print(type(time_stamp))  # <class 'float'>

# 时间戳转datetime
# 引入time和datetime

time_date = datetime.fromtimestamp(time.time())
print(time_date)  # 2023-10-18 11:06:11
print(type(time_date))  # <class 'datetime.datetime'>
