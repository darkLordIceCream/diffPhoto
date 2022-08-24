from util import *


class photo:
    def __init__(self, path):   # 通过util中的函数获取属性
        self.path = path
        self.name = get_photo_name(path)
        self.num = get_num(path)

        self.height, self.width = get_width(self.name[0])
        self.diff = cal_diff(self.width, self.num)

    def cut_and_combine_photo(self):
        cache_dir = self.path + os.sep + 'cache'
        diff = list(self.diff)
        tool = 0

        # 创建一个cache文件夹临时储存切割出来的图片
        if not os.path.exists(cache_dir):
            os.mkdir(cache_dir)
            # 切割图片
            for name, i in zip(self.name, range(0, len(self.name))):
                img = cv2.imdecode(np.fromfile(self.name[i], dtype=np.uint8), -1)   # 中文路径问题，普通的imread可能无法读取
                # img = cv2.imread(self.name[i])
                if not diff[2] == 0:
                    cv2.imencode('.jpg', img[0:self.height, tool:tool + diff[0]])[1].tofile(
                        cache_dir + os.sep + str(i) + '.jpg')   # 同样是中文路径问题，普通的imwrite可能无法写入
                    # cv2.imwrite(cache_dir + os.sep + str(i) + '.jpg', img[0:self.height, tool:tool + diff[0]])
                    diff[2] = diff[2] - 1
                    tool += diff[0]
                else:
                    cv2.imencode('.jpg', img[0:self.height, tool:tool + diff[1]])[1].tofile(
                        cache_dir + os.sep + str(i) + '.jpg')
                    # cv2.imwrite(cache_dir + os.sep + str(i) + '.jpg', img[0:self.height, tool:tool + diff[1]])
                    tool += diff[1]
                os.system('cls')
                log("正在切割")
                print(str(i) + '/' + str(self.num) + "张图片, " + "已完成%" + str(int(i/self.num*100)))

        os.system('cls')
        log("已完成切割")
        # combine
        log("正在合并图片...")
        cache_photo = get_photo_name(cache_dir)
        img = cv2.imdecode(np.fromfile(cache_photo[0], dtype=np.uint8), -1)
        # img = cv2.imread(cache_photo[0])
        for i in range(1, len(cache_photo)):
            img1 = cv2.imdecode(np.fromfile(cache_dir + os.sep + str(i) + '.jpg', dtype=np.uint8), -1)
            # img1 = cv2.imread(cache_dir + os.sep + str(i) + '.jpg')
            img = np.concatenate([img, img1], axis=1)
        cv2.imencode('.jpg', img)[1].tofile(self.path + os.sep + 'combine.jpg')
        # cv2.imwrite(self.path + os.sep + 'combine.jpg', img)
        shutil.rmtree(cache_dir)
        log("合并完成")
