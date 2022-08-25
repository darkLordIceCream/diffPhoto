#
# @file cal_diff.py
#
from . Lib import *


# 因为像素的特殊性，会产生鸡兔同笼问题，详见README
def cal_diff(width, num):
    diff = width / num
    diff_0 = 0
    if int(diff) < diff:    # 判断是否除完
        diff = int(diff)
        diff_0 = diff + 1
    else:
        diff = int(diff)
    y = width - diff * num
    x = num - y
    return diff, diff_0, x, y
