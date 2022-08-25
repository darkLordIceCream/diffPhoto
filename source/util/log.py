#
#  @file log.py
#
from . Lib import *


def log(content):
    """
    在控制台打印日志：时间 ： 内容
    :param content:
    """
    print(datetime.datetime.now(), ":  ", content)