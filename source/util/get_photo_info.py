#
# @file get_photo_name.py
#
from .Lib import *


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

