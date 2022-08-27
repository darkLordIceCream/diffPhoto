# @Time : 2022/8/11-18:20
# @Author : darkLord
# @E-mail : 1712313289@qq.com
# @Github : https://github.com/darkLordIceCream

# coding: utf-8

from util import *
from photo_class import *

#  pyinstaller -F  main.py --paths="E:\Quick Folder\Desktop\GitHub\diffPhoto\venv\Lib\site-packages"
if __name__ == '__main__':
    path = input_path()
    orientation = input_orientation()

    test = photo(path, orientation)
    print_hi('hello world')
    log("diffPhoto start")
    # print(test.name)
    test.cut_and_combine_photo()
    # names = get_photo_name(path)
    # for name in names:
    #     height, width = get_width(name)
    #     if height != 4016:
    #         print(name)
