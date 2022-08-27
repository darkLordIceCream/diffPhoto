from .Lib import *


def input_path():
    path = input('请拖入目录下任意一张图片并按下回车: ')
    # path = r"F:\temp0\_ZFC0789.jpg"
    path = os.path.dirname(path)  # 获取父目录
    if path[0] == '"':
        path = path[1:]  # 如果拖入的文件路径带有空格，路径就会带有双引号，就可能是"C:/a/b"的形式，读取父目录后就成了"C:/a，因此需要做个判断，去掉第一个引号
    return path


def input_orientation():
    orientation = input('从左到右拼扣0，从右到左拼扣1: ')  # 朝向
    if orientation == '0':
        orientation = False
    else:
        orientation = True
    return orientation
