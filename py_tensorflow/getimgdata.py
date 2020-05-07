import numpy as np
import re, os


class GetImageData:
    """
    GetImageData类
    将图片数据处理成ndarry数据
    """
    def __init__(self):
        pass

    # self.dir = dir   # 该文件夹中有多个子文件夹，每个子文件夹名为一个人名，里面是这个人的多张人脸照片

    def onehot(self, numlist=[1, 2, 3, 0, 0]):
        """
        将输入的数字列表转为独热编码的形式
        :param numlist: 数字列表
        :return: 列表中数字的独热编码形式
        """
        b = np.zeros([len(numlist), max(numlist)+1])
        b[np.arange(len(numlist)), numlist] = 1     # 将每个的真实值标为1
        return b


    def getimagenames(self, path=None):
        """
        获取指定文件夹中的JPG图片名称（含路径）
        :param path: 指定文件夹
        :return: path中的所有JPG图片名称（含路径，例如：./path/image1.jpg）
        """
        imagesnames = []
        filenames = os.listdir(path)
        for i in filenames :
            if re.findall('^\d+\.jpg$', i) != []:
                imagesnames.append(path + i)  # 这里的path需要以/结尾，否则需要这样：os.path.join(path, i)
        return imagesnames


    def getfileandlabels(self):
        """
        获取self.dir中每个文件（人名）的独热编码及每个文件（人名）对应的标签（数字）
        :param self.dir: 指定路径，该路径中包含多个文件夹，每个文件夹为一个人的多张照片，文件名为人名
        :return: 返回两个值
        1. 文件名（人名）与其类别的独热编码       # [('./small_img_gray/hexianbin', array([1., 0., 0., 0., 0., 0.])), ...]
        2. 数字标签和文件名（人名）的对应关系     # {0: 'hexianbin', ...}
        """
        dir = './small_img_gray/'
        dirDict = {name: dir + name for name in os.listdir(dir) if os.path.isdir(dir + name)}  # 写法二：os.path.join(dir, name)
        # print(dirDict)  # {'hexianbin': './small_img_gray/hexianbin', ...}
        nameList, pathList = dirDict.keys(), dirDict.values()
        numList = list(range(len(nameList)))  # [0, 1, 2, 3, 4, 5]
        return list(zip(pathList, onehot(numList))),  dict(zip(numList, nameList))


    def readimg(self):
        """
        读取dir中所有图片，将图片数据转为数组，并保存相应标签
        :param dir: 文件夹路径
        :return: 返回三部分的数据
        x: 图片像素数据
        y: 图片标签（0,1,2,3,4,5,...）
        number_name: 数字标签和人名的对应关系（字典）
        """
        #获取文件名（人名）的独热编码和标签信息
        #依次访问各文件名（人名）及对应的独热编码
        #访问某文件名（人名）下的所有图片
        pathLabel, numberName = self.get











