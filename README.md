#【微分摄影】 diffPhoto
#作者 @黑暗之王
#QQ: 1712313289

>起因是B站刷到了刘博洋的视频https://www.bilibili.com/video/BV1PZ4y1r7cc?spm_id_from=333.999.0.0&vd_source=96a826424059577aef56f30578dd6e35， 产生了自己制作的想法，由于太懒，一直拖到假期

>其实之前写过一个demo，但是写着写着发现没这么简单，代码就拧成了一团麻花，毫无可读性、可维护性、可拓展性，也因为操作失误让内存爆满。因此这次用更清晰的逻辑来编写了代码，也给未来拓展这个代码保留了一些空间

>使用方法：
	在任意位置创建一个新文件夹，将拼图素材存进文件夹中，然后运行main.exe程序，将素材文件夹中的任意一张图片拖入程序框中，选择左右顺序，按下回车键即可。
	拼图过程中会在素材文件夹内产生一个cache文件夹，等拼图结束后会消失，请勿移动或删除cache文件夹。
	注意，目前仅支持.jpg图片

******1.2版本2022.08.27******
>通过正则表达式提取数字进行排序
> 解决了字符串排序问题，增加了左右顺序选项
> 将路径获取等放在了util中

******1.1版本2022.08.25******
>修改了文件的结构，将util文件改为一个文件夹，方便拓展、维护与阅读

******1.0版本2022.08.16******
>主要思路：
	延时摄影是将相机架好，使用定时拍摄功能拍摄数张照片，然后后期调色后合成视频的一种摄影形式，这样可以在短短十秒左右的视频中展现如日转夜，或者云朵流动的美丽效果。
	同时，如果把每一张图片切割出一部分，再合并成一张图，我们就可以在一张图里面展现出随时间变化的炫酷效果。
	因此，我们只需要读取素材图片->切割->合并即可。
	拼图会以命名为combine，存放在素材文件夹中

>代码结构：
	source->源代码文件夹
	venv->环境和库
	test_photo->35张测试用的图片
  其中souce文件夹中有main、util、photo_class三个文件
  main文件中定义了文件路径，实现了拖入图片读取路径
  util中是几个函数，主要是一些数据的读取，其中cal_diff是用来解决鸡兔同笼的问题，详见下
  photo_class里面是一个类，单独将一个类写在一个文件是为了方便日后的拓展，若想对其他文件，比如视频做一些操作，直接再添加一个文件即可

>鸡兔同笼问题：
	刘博洋的视频中，他的相机拍摄出的照片宽度为6000像素，他一次性拍摄了6000张素材，因此每张照片只需要切割第一列，再把六千列照片合并即可。
	但是我们日常拍摄很少有拍这么大的量，以我的相机为例，图片宽度为5568像素，如果我拍摄了20张，那理论上来说每张图片就需要切割成宽度为5568/20 = 278.4即可(高度不需要变)。
	因此问题产生，像素是一个具体的物理量，没有小数点，就像不可能有278.4个人。若我们取其整数部分，每张图的宽度切割成278，那么20张图片合并后宽度为5560，损失了一些像素。
	解决这个问题也很简单，就是小学就学过的鸡兔同笼问题，将一部分的图片切割成宽度为278像素，一部分切割成279像素，因此可以列一个方程组：
						设需要将x张图切割成宽度278，y张图需要切割成宽度279，因此有：
								278*x + 279*y = 5568, 
								        x + y = 20.
	解这个方程组也很容易，下式乘以278，再用上式减去下式，可得y = 8，因此x = 12.
	util中的cal_diff函数返回一个数组，以上述的20张图片为例，返回[278, 279, 12, 8]，在photo类中的切割方法中用到。
