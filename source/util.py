import sys
import os
import cv2
import numpy as np
import datetime
import shutil
import msvcrt
import sys
from numpy import unicode


def print_hi(name):
    print(f'{name}')


def log(content):
    """
    在控制台打印日志：时间 ： 内容
    :param content:
    """
    print(datetime.datetime.now(), ":  ", content)


# Get the names in the path
def get_photo_name(path):
    names = []
    for name in os.listdir(path):
        if name.endswith(".jpg") or name.endswith(".JPG"):
            names.append(path + os.sep + name)
    return names


# Get the width of the images
def get_width(name):
    img0 = cv2.imdecode(np.fromfile(name, dtype=np.uint8), -1)
    height, width, c = img0.shape
    return height, width


# Get the numbers of the images
def get_num(path):
    num = 0
    for name in os.listdir(path):
        if name.endswith(".jpg") or name.endswith(".JPG"):
            num = num + 1
    return num


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
