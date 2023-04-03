import os
import sys
import time

# 动态获取项目路径
base_path = os.path.dirname(__file__)
# 获取当前日期
new_time = time.strftime("%Y-%m-%d_%H-%M-%S")
# 获取错误信息 注意：调用是加索引 exec_info[1]才是错误信息
exec_info = sys.exc_info()


# 组装文件路径  如："../image/"
def file_path(filename):
    return base_path + os.sep + filename + os.sep
