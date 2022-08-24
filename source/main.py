# @Time : 2022/8/11-18:20
# @Author : darkLord
# @E-mail : 1712313289@qq.com
# @Github : https://github.com/darkLordIceCream

# coding: utf-8
from util import *
from photo_class import *
#  pyinstaller -F  main.py --paths="E:\Quick Folder\Desktop\diffPhoto\venv\Lib\site-packages"
path = input('请拖入目录下任意一张图片并按下回车: ')
path = os.path.dirname(path)  # 获取父目录
if path[0] == '"':
    path = path[1:]  # 如果拖入的文件路径带有空格，路径就会带有双引号，就可能是"C:/a/b"的形式，读取父目录后就成了"C:/a，因此需要做个判断，去掉第一个引号

if __name__ == '__main__':
    test = photo(path)
    print_hi('hello world')
    log("diffPhoto start")
    test.cut_and_combine_photo()
    # get_photo_name(path)
