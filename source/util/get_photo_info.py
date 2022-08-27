#
# @file get_photo_name.py
#
from .Lib import *


# Get the names in the path
def get_photo_name(path):
    names = []
    for name in os.listdir(path):
        if name.endswith(".jpg") or name.endswith(".JPG") or name.endswith(".jpeg"):
            names.append(path + os.sep + name)
    names.sort(key=lambda l: int("".join(re.findall(r'\d+', l))))   # 通过正则表达式提取数字进行排序
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

